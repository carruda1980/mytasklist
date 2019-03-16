// $(function() {
//     //hang on event of form with id=myform
//     $("#createtask").submit(function(e) {

//         //prevent Default functionality
//         e.preventDefault();

//         //get the action-url of the form
//         var actionurl = e.currentTarget.action;

//         //do your own request an handle the results
//         $.ajax({
//                 url: actionurl,
//                 type: 'post',
//                 dataType: 'application/json',
//                 //data: $("#createtask").serialize(),
//                 // success: function(data) {
//                 //     ... do something with the data...
//                 // }
//         });
//         console.log(data);

//     });

// });


// function CreateTask(){
//     var url = "teste";
//      var titulo = $("#titulo").val();
//     var descricao = $("#descricao").val();
//     $.ajax({
//         url: url,
//         type: "POST",
//         data: {
//             'titulo': titulo,
//             'descricao': descricao,
//             'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
//         },
//         beforeSend: function(){
//             $('ajax-loader').show();
//         }
//     });

//     console.log($('input[name=csrfmiddlewaretorken]').val());
// }