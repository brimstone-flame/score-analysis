# Score Analysis Project
A student score analysis project built with Python, Pandas and Matplotlib. It reads scores from a CSV file, performs statistics and visualizes the results.

## Features
- Load student scores from CSV
- Calculate total scores automatically
- Generate basic statistics (mean, max, min) for each subject
- Analyze scores by class and gender
- Count students who failed each subject
- Rank students by total score
- Visualize results with bar charts

## Project Structure
score-analysis/ ├── score_analysis.py (Main analysis script) ├── scores.csv (Raw student score data) └── README.md (Project description)

## How to Run
1. Clone the repository: `git clone https://github.com/brimstone-flame/score-analysis.git && cd score-analysis`
2. Install dependencies: `pip install pandas matplotlib`
3. Run the script: `python score_analysis.py`

## Data Format (scores.csv)
class,name,gender,chinese,math,english
1,张三,男,85,92,78
1,李四,男,72,68,65
2,小红,女,88,95,90

## License
MIT
