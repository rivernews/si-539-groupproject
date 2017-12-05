// fireDataManager.js
var parameters = {
	"time-start": "0001-1",
	"time-end": "9999-12",
	/** Time [Required]
	 * 
	 * USAGE:
	 * Value range: [0001-1, 9999-12].
	 * start or end time not specified - no data returned.
	 * format is not YY-mm - no data returned.
	 */
	
	"area-min": "100000",
	"area-max": "500000",
	/** Area [Required]
	 * 
	 * USAGE:
	 * Value range: [0, 9999999].
	 * Not specified - no data returned.
	 * 
	 * NOTE:
	 * Actual maximun is 1183539.
	 */
	
	"state": "ALL",
	/** State
	 * 
	 * USAGE:
	 * Value range: [...].
	 * Not specified - no limit.
	 * 'ALL' - no limit.
	 */
	
	"amount": "ALL",
	/** Amount
	 * 
	 * USAGE:
	 * Value range: [0, 99999].
	 * Not specified - default is 10.
	 * 'ALL' - no limit.
	 * '' or not a valid number - not handled.
	 * 
	 * NOTE:
	 * Actual maximum is 19236.
	 */
};


/**
 * 
 * 
 * 
 */


function para_to_get_string(parameters){
	var param_string = "";
	for (var param in parameters){
		var value = parameters[param];
		param_string += param + "=" + value;
		param_string += "&";
	}
	return param_string;
}

function get_fire_data(){

	// check parameter first!

	var xhr = new XMLHttpRequest();
	xhr.open('GET', 'get_data?' + para_to_get_string(parameters));
	xhr.onload = function() {
		if (xhr.status === 200) {
			console.log("ajax succeed la:")
			response = JSON.parse(xhr.responseText);
			console.log(response.row_list);
		}
		else {
			console.log('Request failed.  Returned status of ' + xhr.status);
		}
	};
	xhr.send();
}

