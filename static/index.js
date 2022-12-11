$(document).ready(function(){
	// $('#Translate-btn').click(function(){
    //     console.log('cliquei')
	// 	var input = $('#input').val();
    //     console.log(input)
	// 	$.ajax({
	// 		url: '/',
    //         contentType: 'application/json;charset=UTF-8',
            
    //         data : input,
	// 		type: 'POST',
	// 		success: function(response){
    //             const output = document.getElementById('output');
    //             output.textContent = response
	// 			console.log(response);
	// 		},
	// 		error: function(error){
	// 			console.log(error);
	// 		}
	// 	});
	// });
    const output = document.getElementById('output');

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
                    output.textContent = response
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