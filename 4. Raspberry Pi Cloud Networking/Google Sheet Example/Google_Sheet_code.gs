//Google sheet id : [Enter your sheet id here]
//Current url : [Enter URL here]
//Sample url : [Enter URL here with sample parameters]

//-----------------------------------------------

/**
* Function doGet: Parse received data from GET request, 
  get and store data which is corresponding with header row in Google Spreadsheet
*/

function doGet(e){ 
  Logger.log( JSON.stringify(e) );                  // view parameters
  var result = ''; // assume success
  var sheet;

  if (e.parameter == 'undefined') {                 // Stop Script if there are no parameters in GET request
    result = 'No Parameters';
  }                                            
  else {
    var sheet_id = [/*Enter your sheet id here*/]; 		
    // Spreadsheet ID
    var spreadSheet = SpreadsheetApp.openById(sheet_id);
    // get Active sheet
    var newRow;			
    var rowData = [];
    //sheet=spreadSheet.getActiveSheet;
    sheet = spreadSheet.getSheetByName("Sheet1");
    newRow = sheet.getLastRow() + 1;
    
    for (var param in e.parameter)                                      // Loop through all query parameters
    {                                               
      Logger.log('In for loop, param=' + param);
      var value = stripQuotes(e.parameter[param]);
      Logger.log(param + ':' + e.parameter[param]);
      
      switch (param) {
          // Case: value - To input sensor value in sheet
          case 'value':
            rowData[0] = new Date();                                       // Timestamp in column A
            rowData[1]=value;                                              // Sensor Value in column B
            var newRange = sheet.getRange(newRow, 1, 1, rowData.length);   // Select last row of sheet
            newRange.setValues([rowData]);                                 // Set values in last row
            result += "Written on column Value";                         // Response Text (Optional)
            return ContentService.createTextOutput(result);
            break;       
          
          // Case: get - To output sensor value to user
          case 'get':
            if(value==0)                                                        // Output all rows
            {
              data = sheet.getDataRange().getValues();
              for (var i = 1; i < data.length; i++) 
              {
                result+=data[i][0]+","+data[i][1]+"<br>";
              }//end of for
              return ContentService.createTextOutput(result);
            }
            else
            {                                                              // Output a particular row number = value
              data = sheet.getDataRange().getValues();
              i=value;
              result=data[i][0]+","+data[i][1]+"<br>";
              return ContentService.createTextOutput(result);
            }
            break;
          
          default:
            result = "unsupported parameter";
        }// end of switch
    }// end of for
    
    //Logger.log(JSON.stringify(rowData));
  }

}
/**
* Remove leading and trailing single or double quotes
*/
function stripQuotes( value ) {
  return value.replace(/^["']|['"]$/g, "");
}

                




//-----------------------------------------------
// End of Script
//-----------------------------------------------





