import numpy as np
import pandas as pd


def create_feature_column(df: pd.DataFrame) -> pd.DataFrame:
    df['over2.5Goals'] = np.where(df['homeGoals'] + df['awayGoals'] > 2, 1, 0)

    return df


def create_match_information_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a dataframe of reduced data containing basic match information
    """
    match_cols = [
        'matchID',
        'date',
        'season',
        'homeTeam',
        'homeGoals',
        'awayTeam',
        'awayGoals',
    ]

    team_info = df[match_cols].copy()

    return team_info


def revert_elos_to_mean(current_elos, soft_reset_factor):
    """
    Used to soft reset ELOs when a new seasons data is provided
    """
    elos_mean = np.mean(list(current_elos.values()))

    new_elos_dict = {
        team: (team_elo - elos_mean) * soft_reset_factor + elos_mean for team, team_elo in current_elos.items()
    }

    return new_elos_dict


def elo_calculator(df, k_factor, historic_elos, soft_reset_factor, match_id_column):
    """
    Calculate rolling ELO ratings for teams based on results provided in dataframe
    """
    # Initialise a dictionary with default elos for each team
    for team in df['homeTeam'].unique():
        if team not in historic_elos.keys():
            historic_elos[team] = 1500

    elo_dict = historic_elos.copy()
    elos, elo_probs = {}, {}

    last_season = 0

    # Loop over the rows in the DataFrame
    for index, row in df.iterrows():
        # Get the current year
        current_season = row['season']

        # If it is a new season, soft-reset elos
        if current_season != last_season:
            elo_dict = revert_elos_to_mean(elo_dict, soft_reset_factor)

        # Get the Game ID
        match_id = row[match_id_column]

        # Get the team and opposition
        home_team = row['homeTeam']
        away_team = row['awayTeam']

        # Get the team and opposition elo score
        home_team_elo = elo_dict[home_team]
        away_team_elo = elo_dict[away_team]

        # Calculated the probability of winning for the team and opposition
        prob_win_home = 1 / (1 + 10 ** ((away_team_elo - home_team_elo) / 400))
        prob_win_away = 1 - prob_win_home

        # Add the elos and probabilities our elos dictionary and elo_probs dictionary based on the Match ID
        elos[match_id] = [home_team_elo, away_team_elo]
        elo_probs[match_id] = [prob_win_home, prob_win_away]

        margin = row['homeGoals'] - row['awayGoals']

        new_home_team_elo = home_team_elo
        new_away_team_elo = away_team_elo

        # Calculate the new elos of each team
        if margin == 1:  # Team wins; update both teams' elo
            new_home_team_elo = home_team_elo + k_factor * (1 - prob_win_home) * 1
            new_away_team_elo = away_team_elo + k_factor * (0 - prob_win_away) * 1
        elif margin == 2:
            new_home_team_elo = home_team_elo + k_factor * (1 - prob_win_home) * 1.5
            new_away_team_elo = away_team_elo + k_factor * (0 - prob_win_away) * 1.5
        elif margin == 3:
            new_home_team_elo = home_team_elo + k_factor * (1 - prob_win_home) * 1.75
            new_away_team_elo = away_team_elo + k_factor * (0 - prob_win_away) * 1.75
        elif margin > 3:
            new_home_team_elo = home_team_elo + k_factor * (1 - prob_win_home) * 1.75 * (margin - 3) / 8
            new_away_team_elo = away_team_elo + k_factor * (0 - prob_win_away) * 1.75 * (margin - 3) / 8
        elif margin == -1:  # Away team wins; update both teams' elo
            new_home_team_elo = home_team_elo + k_factor * (0 - prob_win_home) * 1
            new_away_team_elo = away_team_elo + k_factor * (1 - prob_win_away) * 1
        elif margin == -2:  # Away team wins; update both teams' elo
            new_home_team_elo = home_team_elo + k_factor * (0 - prob_win_home) * 1.5
            new_away_team_elo = away_team_elo + k_factor * (1 - prob_win_away) * 1.5
        elif margin == -3:  # Away team wins; update both teams' elo
            new_home_team_elo = home_team_elo + k_factor * (0 - prob_win_home) * 1.75
            new_away_team_elo = away_team_elo + k_factor * (1 - prob_win_away) * 1.75
        elif margin < -3:  # Away team wins; update both teams' elo
            new_home_team_elo = home_team_elo + k_factor * (0 - prob_win_home) * 1.75 * (margin - 3) / 8
            new_away_team_elo = away_team_elo + k_factor * (1 - prob_win_away) * 1.75 * (margin - 3) / 8
        elif margin == 0:  # Drawn game' update both teams' elo
            new_home_team_elo = home_team_elo + k_factor * (0.5 - prob_win_home) * 1
            new_away_team_elo = away_team_elo + k_factor * (0.5 - prob_win_away) * 1

        # Update elos in elo dictionary
        elo_dict[home_team] = new_home_team_elo
        elo_dict[away_team] = new_away_team_elo

        last_season = current_season

    return elos, elo_probs, elo_dict


def map_formations(df: pd.DataFrame) -> pd.DataFrame:
    formation = {
        1: '5-4-1',
        2: '5-3-2',
        3: '3-5-1-1',
        4: '3-5-2',
        5: '4-5-1',
        6: '3-4-2-1',
        7: '3-4-1-2',
        8: '3-2-4-1',
        9: '4-3-2-1',
        10: '4-3-1-2',
        11: '3-1-4-2',
        12: '4-1-3-2',
        13: '4-2-3-1',
        14: '3-4-3',
        15: '3-3-1-3',
        16: '4-4-1-1',
        17: '4-4-2',
        18: '4-1-4-1',
        19: '4-2-2-2',
        20: '4-3-3'
    }

    formation = {v: k for k, v in formation.items()}

    df.replace(formation, inplace=True)

    return df


def drop_non_features(df: pd.DataFrame) -> pd.DataFrame:
    columns = [
        'date',
        'season',
        'homeTeamID',
        'homeGoals',
        'awayTeamID',
        'awayGoals',
    ]

    df.drop(columns, axis=1)

    return df

