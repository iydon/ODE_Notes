all:
	xelatex note
	xelatex note
	rm *.aux *.log *.synctex *.thm *.toc
clean:
	rm *.aux *.log *.synctex *.thm *.toc