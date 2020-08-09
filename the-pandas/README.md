# Install Pandas

    pip install pandas

    Help on pandas function:

        pandas.read_csv? -> This will output the help instructions

# Install interactive python
    
    pip install ipython

# Install jupyter

    pip install jupyter

    Run Jupter:

        Go to directory where notebook needs to be created and run:

            jupyter notebook   


# DataFrame is object which represents row, column structure

    a) Create a DataFrame from list with column:
        df1 = pandas.DataFrame([[2,3,4],[5,6,7]], columns=["col1", "col2", "col3"])
    
    b) Create a DataFrame with dictionary:
        df1 = pandas.DataFrame([{ "first_name":"Sahil", "last_name" : "Patayar" }, { "first_name":"John", "last_name" : "Wick" }] )

    c) if data does not have header, provide header=None as argument, pandas will create default header