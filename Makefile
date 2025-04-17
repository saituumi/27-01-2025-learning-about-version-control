
all: results/clean_penguins.csv \
	results/bill_length_boxplot.png\
	results/predictions.csv results/classification_report.txt\
	results/confusion_matrix.png \
	reports/report.html \
	reports/report.ipynb




results/clean_penguins.csv : scripts/01_load_data.py
	python scripts/01_load_data.py clean_penguins.csv 

results/bill_length_boxplot.png: results/clean_penguins.csv scripts/02_methods.py
	python scripts/02_methods.py results/clean_penguins.csv 


results/predictions.csv results/classification_report.txt : results/clean_penguins.csv scripts/03_model.py
	python scripts/03_model.py --data_path=results/clean_penguins.csv

results/confusion_matrix.png : results/clean_penguins.csv scripts/04_results.py
	python scripts/04_results.py --data_path=results/clean_penguins.csv --model_path=results/penguin_model.pkl

reports/report.html: report.qmd
	mkdir -p reports
	quarto render report.qmd --to html --output-dir reports

reports/report.ipynb: report.qmd
	mkdir -p reports
	quarto render report.qmd --to ipynb --output-dir reports

clean:
	rm -rf results/*
	rm -rf reports/*


