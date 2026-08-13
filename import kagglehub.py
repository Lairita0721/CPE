import kagglehub

# Download latest version
path = kagglehub.competition_download('lab-04-fruit-classification')

print("Path to competition files:", path)