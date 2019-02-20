all:
	xelatex note
	xelatex note
	rm *.aux *.log *.thm *.toc
clean:
	rm *.aux *.log *.thm *.toc	