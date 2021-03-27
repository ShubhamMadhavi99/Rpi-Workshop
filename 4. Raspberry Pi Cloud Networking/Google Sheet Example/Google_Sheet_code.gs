//Google sheet id : [Enter your sheet id here]
//Current url : [Enter URL here]
//Sample url : [Enter URL here with sample parameters]

//-----------------------------------------------

/**
* Function doGet: Parse received data from GET request, 
  get and store data which is corresponding with header row in Google Spreadsheet
*/

function doGet(e){ 
  Logger.log( JSON.stringify(e) );              // view parameters
  var result = ''; // assume success
  var sheet;

  if (e.parameter == 'undefined') {             // C=Stop Script if there are no parameters in GET request
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
    
    for (var param in e.parameter) {
      Logger.log('In for loop, param=' + param);
      var value = stripQuotes(e.parameter[param]);
      Logger.log(param + ':' + e.parameter[param]);
      
      switch (param) {
          
          case 'roll':
          //rowData[0] = new Date();                                       // Timestamp in column A
          //rowData[1] = new Date().toLocaleTimeString();
          rowData[0]=value;
          result += 'Written on column Roll No';
          break;       
          
          case 'name': //Parameter
          rowData[1] = value; 
          result += 'Written on column name';
          break;
        case 'attd': //Parameter
          rowData[2]=value;
          rowData[3]=((value>75)?'Y':'N');
          result += ' ,Written on column Attendance';
          break;  
          
          case 'get':
          if(value==0) //fetch all rows
          {
           data = sheet.getDataRange().getValues();
          for (var i = 1; i < data.length; i++) {
    result+=data[i][0]+","+data[i][1]+","+data[i][2]+","+data[i][3]+";";
          }//end of for
            return ContentService.createTextOutput(result);
          }
          else{  //fetch a particular row
           data = sheet.getDataRange().getValues();
           i=value;
           result=data[i][0]+","+data[i][1]+","+data[i][2]+","+data[i][3];
            return ContentService.createTextOutput(result);
          }
          break;
          
        default:
          result = "unsupported parameter";
      }
    }
    Logger.log(JSON.stringify(rowData));
    // Write new row below
    var newRange = sheet.getRange(newRow, 1, 1, rowData.length);
    newRange.setValues([rowData]);
  }
  // Return result of operation
  return ContentService.createTextOutput(result);
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





