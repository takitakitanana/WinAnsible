from shadow import user, splunk

state = [

    # syslog collectors
    ['1', 'lue1vp10204', 'syslog', False, 0, 0, 0, 0, splunk['u'], splunk['p'], '54.41.8.36', 2022],    
    ['2', 'lctcvp6227', 'syslog', False, 0, 0, 0, 0, user['u'], user['p'], '54.56.168.82', 2022],
    # belgium
    ['3', 'lamevp1000', 'syslog', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.101.204.6', 2022],
    ['4', 'lamevp1001', 'syslog', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.101.204.7', 2022],
    ['5', 'lamevp1002', 'syslog', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.101.204.8', 2022],
    # us    
    ['6', 'lctcvp7820', 'syslog', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.58.40.236', 2022],    
    ['7', 'lctcvp7821', 'syslog', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.58.41.68', 2022],    
    ['8', 'lctcvp7822', 'syslog', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.58.41.26', 2022],
    # singapore     
    ['9', 'lskcvp6643', 'syslog', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.58.40.14', 2022],     
    ['10', 'lskcvp6642', 'syslog', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.120.96.134', 2022],

    # aws on-prem   
    ['11', 'lue1vp1012', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.27.210', 2022],  
    ['12', 'lue1vp1024', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.13.111', 2022], 
    ['13', 'lue1vp1025', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.13.61', 2022], 
    ['14', 'lue1vp1026', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.1.36', 2022],  
    ['15', 'lue1vp1027', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.13.71', 2022],   
    ['16', 'lue1vp1028', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.1.79', 2022],  
    ['17', 'lue1vp1030', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.10.246', 2022],  
    ['18', 'lue1vp11642', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '10.62.164.109', 2022],
    ['19', 'lue1vp11643', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '10.62.166.44', 2022],
    ['20', 'lue1vp11644', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '10.62.161.201', 2022],
    ['21', 'lue1vp11659', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '10.62.166.129', 2022],
    ['22', 'lctcsp1020', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.56.139.152', 2022], 
    ['23', 'lue1vp12213', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '10.62.162.218', 2022],
    ['24', 'lctcvp1186', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '155.91.32.206', 2022], 
    ['25', 'lctcvp1220', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '155.91.32.8', 2022],   
    ['26', 'lctcvp7021', 'aws-prem', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.58.5.237', 2022],

    # phantom   
    ['27', 'lue1vd7375', 'phantom', False, 0, 0, 0, 0, user['u'], user['p'], '54.41.8.114', 2022],
    ['28', 'lue1vd7377', 'phantom', False, 0, 0, 0, 0, user['u'], user['p'], '54.41.4.222', 2022],
    ['29', 'lue1vp1037', 'phantom', False, 0, 0, 0, 0, user['u'], user['p'], '54.41.4.25', 2022],
    ['30', 'lue1vp1038', 'phantom', False, 0, 0, 0, 0, user['u'], user['p'], '54.41.12.101', 2022],
    ['31', 'lue1vt1028', 'phantom', False, 0, 0, 0, 0, user['u'], user['p'], '54.41.14.9', 2022],
    ['32', 'lue1vt10210', 'phantom', False, 0, 0, 0, 0, user['u'], user['p'], '54.41.4.180', 2022],

    ### CUSTOM GORUPS ###
    ############################# Test Group #############################
    ['0', 'lue1vp10204', 'test', False, 0, 0, 0, 0, splunk['u'], splunk['p'], '54.41.8.36', 2022],
    ['0', 'lamevp1000', 'test', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.101.204.6', 2022],
    ['0', 'lctcvp7820', 'test', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.58.40.236', 2022],
    ['0', 'lskcvp6643', 'test', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.58.40.14', 2022],
    ['0', 'lue1vp1012', 'test', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.27.210', 2022],
    ['0', 'lue1vd7375', 'test', False, 0, 0, 0, 0, user['u'], user['p'], '54.41.8.114', 2022],   

    ################################### ALL GROUP ###################################
    # syslog collectors
    ['0', 'lue1vp10204', 'all', False, 0, 0, 0, 0, splunk['u'], splunk['p'], '54.41.8.36', 2022],    
    ['0', 'lctcvp6227', 'all', False, 0, 0, 0, 0, user['u'], user['p'], '54.56.168.82', 2022],
    # belgium
    ['0', 'lamevp1000', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.101.204.6', 2022],
    ['0', 'lamevp1001', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.101.204.7', 2022],
    ['0', 'lamevp1002', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.101.204.8', 2022],
    # us    
    ['0', 'lctcvp7820', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.58.40.236', 2022],    
    ['0', 'lctcvp7821', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.58.41.68', 2022],    
    ['0', 'lctcvp7822', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.58.41.26', 2022],
    # singapore     
    ['0', 'lskcvp6643', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.58.40.14', 2022],     
    ['0', 'lskcvp6642', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.120.96.134', 2022],
    # aws on-prem   
    ['0', 'lue1vp1012', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.27.210', 2022],  
    ['0', 'lue1vp1024', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.13.111', 2022], 
    ['0', 'lue1vp1025', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.13.61', 2022], 
    ['0', 'lue1vp1026', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.1.36', 2022],  
    ['0', 'lue1vp1027', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.13.71', 2022],   
    ['0', 'lue1vp1028', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.1.79', 2022],  
    ['0', 'lue1vp1030', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.41.10.246', 2022],  
    ['0', 'lue1vp11642', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '10.62.164.109', 2022],
    ['0', 'lue1vp11643', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '10.62.166.44', 2022],
    ['0', 'lue1vp11644', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '10.62.161.201', 2022],
    ['0', 'lue1vp11659', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '10.62.166.129', 2022],
    ['0', 'lctcsp1020', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.56.139.152', 2022], 
    ['0', 'lue1vp12213', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '10.62.162.218', 2022],
    ['0', 'lctcvp1186', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '155.91.32.206', 2022], 
    ['0', 'lctcvp1220', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '155.91.32.8', 2022],   
    ['0', 'lctcvp7021', 'all', True, user['u'], user['p'], splunk['j'], 2022, splunk['u'], splunk['p'], '54.58.5.237', 2022],
    # phantom   
    ['0', 'lue1vd7375', 'all', False, 0, 0, 0, 0, user['u'], user['p'], '54.41.8.114', 2022],
    ['0', 'lue1vd7377', 'all', False, 0, 0, 0, 0, user['u'], user['p'], '54.41.4.222', 2022],
    ['0', 'lue1vp1037', 'all', False, 0, 0, 0, 0, user['u'], user['p'], '54.41.4.25', 2022],
    ['0', 'lue1vp1038', 'all', False, 0, 0, 0, 0, user['u'], user['p'], '54.41.12.101', 2022],
    ['0', 'lue1vt1028', 'all', False, 0, 0, 0, 0, user['u'], user['p'], '54.41.14.9', 2022],
    ['0', 'lue1vt10210', 'all', False, 0, 0, 0, 0, user['u'], user['p'], '54.41.4.180', 2022],
    ################################### ALL GROUP ###################################
]
