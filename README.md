# UZH Data Science Project

Analyzing the NBA dataset in the scope of the course ESC403 - introduction to
data science at the University of Zurich (UZH).


## Project Proposal and Motivation

In basketball, specifically the NBA, data-driven insights are becoming
increasingly important each season, helping teams shape their rosters and
strategic approaches. This project aims to explore historical NBA data such as
box scores and advanced statistics of both players and teams to analyze
patterns in which metrics define a games outcome (Win/Loss), such as gameplay
metrics and financial investment.


## Research Questions and Analytical Objectives

1. Home-court advantage: Does home-court advantage exist and how large is it?
2. Winning vs loosing: Can we identify statistical differences between winning
   and loosing teams?
3. Temporal trends: How has the game evolved over the years? Can we
   differentiate the data into eras of how the game was played?
   - [ts_team_analysis](./ts_team_analysis.ipynb)
   - [ts_team_prediction](./ts_team_prediction.ipynb)
4. Financial influence: Is there a correlation between the teams expenditure on
   the roster and team success? Does the salary cap affect long-term success?
5. Game outcome prediction: Can box scores predict which team will win? Can we
   use the temporal trends to predict a winning team?


Each question is discussed in more detail with what each file is responsible
for below in the *Procedure* section.


## Data Source and Description 

1. [Historical NBA Data and Player Box
   Scores](https://www.kaggle.com/datasets/eoinamoore/historical-nba-data-and-player-box-scores/code):
   This dataset includes game statistics (e.g., points assists, rebounds) of
   both players and teams, spanning all the way back to 1946.
2. [NBA API](https://github.com/swar/nba_api?tab=readme-ov-file): If the need
   arises for more advanced statistics, we will use this Python wrapper of the
   official NBA API, which includes advanced player and team metrics.


## Procedure

1. Get data and clean data to do EDA and create dataset we can use for
   subsequent analysis
   - [get_data](./get_data.ipynb)
   - [clean_data](./clean_data.ipynb)
   - [clean_team_data](./clean_team_data.ipynb)
   - [clean_data](./clean_data.ipynb)
2. Answering the research questions (see above)
3. Cleanup and presentation


### Home-Court Advantage 

[home_court_advantage](./home_court_advantage.ipynb)
- Does the home team win more often than the away team?
- Do the referees call fewer fouls on the home team (i.e. the home team gets
  more free throws than the away team)?
- If the home team wins, does it win by a larger margin than if the away team
  wins?
- Does the home team score on a higher percentage (FG%, FT%, 3P%) than the away
  team?
- **Conclusion**:
  - Home team does win with a higher percentage than the away team.
  - Home teams do have better statistics in all categories, though we cannot
    conculde yet if it is significant.
  - The home team does win more often.
  - The home team does not get the same amount of fouls as the away team. 
  
  
### Winning Teams

[winning_teams](./winning_teams.ipynb)
- 


## Run Code

How to run and configure the code. 


### Config File

```yaml
---
data_path: ""
use_drive: false
...
```

- `data_path`: Set to the path of the directory where the data (.csv files) is
  stored. (E.g. `"./"`)
- `use_drive`: Set to true if you are running on google colab and would like to
  mount your personal drive. Make sure to have the `data_path` set accordingly.


