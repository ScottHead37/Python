<#
.Synopsis
   Test to quickly check winRM acess to machines
.DESCRIPTION
   Takes input from text file and runs function to test WinRm
.EXAMPLE
   WinRM-Status $ComputerList
#>

Function WinRM-Status($Computers){    
    
    #Test Path to each system and throttle limit of concurrnet processes to 256
    $WinRMJob = Invoke-Command -ScriptBlock {Test-Path "C:\"} -ComputerName $Computers  -ThrottleLimit 256 -AsJob | Wait-Job

    #Group the results together, then sort into 2 string arrays with servername only
    $Grouped = $WinRMJob.ChildJobs | Group-Object -Property State
  
    #Pulls Successfule items to one array
    [Array]$WinrmSuccess = ($Grouped | where {$_.Name -eq "Completed"}).Group | %{$_.Location}

    #Pulls Failed Items to another array
    [Array]$noWinrm = Compare-Object -ReferenceObject $Computers -DifferenceObject $WinrmSuccess | Select-Object -ExpandProperty  Inputobject -ErrorAction SilentlyContinue

    #Assigns Array values to object
    $properties = @{               
                WinRMFails = $noWinrm;               
                WinRMPass = $WinrmSuccess;                    
    }
    
    #Create Object and Assign to Var
    $ReturnObj = New-Object -TypeName PSObject -Property $properties

    #Returns the Value
    Return $ReturnObj
}

#Get List of Systems to be Checked.
$ComputerList=Get-Content C:\temp\MyComputers.txt

#Runs the Function and Applies list of Computers
$Results=WinRM-Status $ComputerList

#Output to Screen
$Results.WinRMPass

#Output to Screen
$Results.WinRMFails 
