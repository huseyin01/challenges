def weekdays_graph(resample_daily_list):
    #The days to loop over
    from collections import defaultdict
    from datetime import timedelta
    import pandas as pd
    from datetime import datetime
    import matplotlib.pyplot as plt
    
    day_list = ['Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday']
    #Create a dict for holding the running counts 
    
    avg_index = defaultdict(int)
    for i, t in enumerate(pd.timedelta_range(0, periods=24*4, freq='15T')):
        avg_index[i] = datetime.strptime(str(t).replace('0 days ',''), '%H:%M:%S').time()
    
    #Loop over the 7 days
    for i in range(len(day_list)):
        
        #Create the dataframe to hold the running counts
        avg_df = pd.DataFrame(avg_index.items(), columns=['login', 'login_time'])
        avg_df.login = 0
        avg_df.set_index('login_time', inplace=True)
        
        #Run through grouped day list
        day_range = range(i, len(resample_daily_list), len(day_list))
            
        for j in day_range:
                
            #Extract the dataframe
            df1 = resample_daily_list[j]
            df1 = df1.set_index(df1.index.to_series().dt.time)
                
            #Add the values of this dataframe to running count
            avg_df = avg_df.add(df1, fill_value=0) 
                
            #Plot the time series
            plt.rcParams['figure.figsize']=[15,5]
            if j < len(day_list):
                ax = df1.plot(legend=False, color='lightpink')
            else:
                df1.plot(ax=ax, legend=False, color='lightpink')
        
        #Create the average and plot    
        avg_df['Average'] = avg_df['count']/float(len(day_range))
        avg_df.drop(['login','count'], axis=1, inplace=True)
        avg_df.plot(ax=ax, legend=True, color='darkred', lw=4.)
        
        #Plot the full graph
        ax.set_title('All ' + day_list[i] + 's')
        ax.set_xlabel('Login Time')
        ax.set_ylabel('Counts')
    return plt.show()

def alldays_graph(resample_daily_list):
    #The days to loop over
    from collections import defaultdict
    from datetime import timedelta
    import pandas as pd
    from datetime import datetime
    import matplotlib.pyplot as plt
    
    
    #Create a dict for holding the running counts 
    avg_index = defaultdict(int)
    for i, t in enumerate(pd.timedelta_range(0, periods=24*4, freq='15T')):
        avg_index[i] = datetime.strptime(str(t).replace('0 days ',''), '%H:%M:%S').time()
    
    #Loop over the 7 days
    for i in range(1):
        
        #Create the dataframe to hold the running counts
        avg_df = pd.DataFrame(avg_index.items(), columns=['login', 'login_time'])
        avg_df.login = 0
        avg_df.set_index('login_time', inplace=True)
        #Run through grouped day list
        day_range = range(i, len(resample_daily_list))
            
        for j in day_range:
                
            #Extract the dataframe
            df1 = resample_daily_list[j]
            df1 = df1.set_index(df1.index.to_series().dt.time)
                
            #Add the values of this dataframe to running count
            avg_df = avg_df.add(df1, fill_value=0) 
                
            #Plot the time series
            plt.rcParams['figure.figsize']=[15,5]
            if j < 1:
                ax = df1.plot(legend=False, color='lightpink')
            else:
                df1.plot(ax=ax, legend=False, color='lightpink')
        
        #Create the average and plot    
        avg_df['Average'] = avg_df['count']/float(len(day_range))
        avg_df.drop(['login','count'], axis=1, inplace=True)
        avg_df.plot(ax=ax, legend=True, color='darkred', lw=4.)
        
        #Plot the full graph
        ax.set_title('All Days')
        ax.set_xlabel('Login Time')
        ax.set_ylabel('Counts')
    return plt.show()