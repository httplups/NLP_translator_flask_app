$(document).ready(function(){
    const output = document.getElementById('output');
    const hostname = document.getElementById('hostname');

    $('#input').on('input', function() {
		var input = $('#input').val();
        input = input.trim()

        if (input != "") {
            $.ajax({
                url: '/',
                contentType: 'application/json;charset=UTF-8',
                
                data : input,
                type: 'POST',
                success: function(response){
                    // console.log(response)
                    output.textContent = response['translated_text']
                    // hostname.textContent = response['hostname']
                },
                error: function(error){
                    console.log(error);
                }
            });
        }
        else {
            output.textContent = ""
        }
	});
});