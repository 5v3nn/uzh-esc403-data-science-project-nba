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
      - Makes calls to the NBA API to obtain player and team statistics.
   - [clean_data](./clean_data.ipynb)
   - [clean_team_data](./clean_team_data.ipynb)
      - Cleans the team statistics, mostly by removing NA rows and useless rows.
      - Only selecting Regular Season games
      - DISCONTINUED due to the fact we swapped from the Kaggle Dataset to the NBA API
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
- Identify important features on normalized box-score statistics
   - Almost half of the columns could be eliminated due to multicollinearity
- Defensive Rebounds & True Shooting % the key variables to predict the current game's win.
   - We think, Defensive Rebounds is the only defensive metric that can directly measure how well the opponent shoots (More rebounds if they shoot poorly)
   - True Shooting represents most of the offensive efficiency  


### Temporal Analysis 

[ts_team_analysis](./ts_team_analysis.ipynb)
- Using the default team statistics dataset
  - Seasonal decomposing: First of `teamScore` and then other features
  - Trying ARIMA on that 
- Using normalized data set
  - Seasonal decompose of "as-is"
  - Then uniform time stamps, since we do not care about the the time in the
    off-season for our precictions (index which only keeps order, not time
    between the games)
    - Still not clear trend
  - Analyze major rule changes to see if there are epochs
    - Seasonal decompose each epoch, fitting trend with linear regression in
      order to find out if rule changes had an effect on or changed the trend


[ts_team_prediction](./ts_team_prediction.ipynb)
- With uniform time index again: ARIMA for `teamScore`, `teamScore_decomposed`
  (`teamScore`, but removed the variance and error), `teamScore_rollingmean`
  - Try to make forecast on those, but not really successful
- Forecast of `teamScore`, but only use a limited time-span (e.g. last 5
  years), because for the current prediction in 2025, the 1980 games are
  objectively not relevant anymore
  - Works better (predicts trend, but not fluctuations)
- **Conclusion**: Hard to impossible to accurately predict the score, just
  based on the previous scores.

### Win Prediction Modeling

[windowed_stats](./windowed_stats.ipynb)
- Create and save windowed rolling statistics so that we can predict future games from the previous averages. For example, if the window size is 5, for each game entry it maintains for each box score statistics the teams and opponent teams the previous 5 game averages.
[prediction](./prediction.ipynb)
- Build Prediction Models to predict whether a team wins a specific game. Used Logistic Regression, Random Forest, XGBoost, Catboost, LightGBM, and Gaussian Naive Bayes as well as an ensemble model of all mentioned models.
- We achieved a best test accuracy of 64.5% with the Logistic Regression Model. Put into perspectice, this is not too bad because there is an upset rate of 22-36% depending on whose odds and model you choose, so a perfect model can achieve 64-78% accuracy. We have only used team statistics and whether a team plays at home, so it is a fairly basic model.


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


