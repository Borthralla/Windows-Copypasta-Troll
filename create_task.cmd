SCHTASKS /Create /TN "copypasta" /TR "%userprofile%\AppData\Local\Programs\Python\Python37\python.exe %cd%\copypasta.pyw" /SC MINUTE /MO 1