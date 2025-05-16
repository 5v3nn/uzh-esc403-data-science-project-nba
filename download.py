import kagglehub

# Download latest version
path = kagglehub.dataset_download("omarsobhy14/nba-players-salaries")

print("Path to dataset files:", path)