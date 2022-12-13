$(document).ready(function(){
    const output = document.getElementById('output');

    // $('#input').on('input', function() {
    $('#input').focusout(function() {
		var input = $('#input').val();
        input = input.trim()

        if (input != "") {
            $.ajax({
                url: '/',
                contentType: 'application/json;charset=UTF-8',
                
                data : input,
                type: 'POST',
                success: function(response){
                    output.textContent = response['translated_text']
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