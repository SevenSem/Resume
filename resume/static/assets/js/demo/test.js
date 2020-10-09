$(document).ready(function(){
    var i=1;
    $("#add_row").click(function(){b=i-1;
      	$('#addr'+i).html($('#addr'+b).html()).find('td:first-child').html(i+1);
      	$('#tab_logic').append('<tr id="addr'+(i+1)+'"></tr>');
      	i++;
  	});
    $("#delete_row").click(function(){
    	if(i>1){
		$("#addr"+(i-1)).html('');
		i--;
		}
		calc();
	});

	$('#tab_logic tbody').on('keyup change',function(){
		calc();
	});
	$('#paid').on('keyup change',function(){
		calc_total();
	});


});


function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+-)');
    var replacement = prefix + '-' + ndx + '-';
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex,
    replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}

function addForm(btn, prefix) {
    console.log(prefix)
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if(prefix == 'educationalInfo'){
        if (formCount < 1000) {
        var row = $(".education:last").clone(false).get(0);
        $(row).removeAttr('id').hide().insertAfter(".education:last").slideDown(30);
        foraddform();

    } // End if
    }else if(prefix == 'experienceInfo'){
        if (formCount < 1000) {
            var row = $(".experience:last").clone(false).get(0);
            $(row).removeAttr('id').hide().insertAfter(".experience:last").slideDown(30);
            foraddform();

    } // End if
    } else if(prefix == 'skills'){
        if (formCount < 1000) {
            var row = $(".skill:last").clone(false).get(0);
            $(row).removeAttr('id').hide().insertAfter(".skill:last").slideDown(30);
           foraddform();

    } // End if
    }else if(prefix == 'certificate'){
        if (formCount < 1000) {
            // Clone a form (without event handlers) from the first form
            var row = $(".certificate:last").clone(false).get(0);
            $(row).removeAttr('id').hide().insertAfter(".certificate:last").slideDown(30);
             foraddform();


    } // End if
    }else if(prefix == 'language'){
        if (formCount < 1000) {
            var row = $(".language:last").clone(false).get(0);
            $(row).removeAttr('id').hide().insertAfter(".language:last").slideDown(30);
         foraddform();

        } // End if
    }
    return false;
}

function foraddform(){
   $(".errorlist", row).remove();
        $(row).children().removeClass("error");

        // Relabel or rename all the relevant bits
        $(row).find('.form-control').each(function () {
            updateElementIndex(this, prefix, formCount);
            $(this).val('');
            $(this).removeAttr('value');
            $(this).prop('checked', false);
        });

        $(row).find(".delete").click(function () {
            return deleteForm(this, prefix);
        });
        // Update the total form count
        $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);
}

function deleteForm(btn, prefix) {
      var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
      if (formCount > 1) {
          var goto_id = $(btn).find('input').val();
          if( goto_id ){
            $.ajax({
                url: "/" + window.location.pathname.split("/")[1] + "/formset-data-delete/"+ goto_id +"/?next="+ window.location.pathname,
                error: function () {
                  console.log("error");
                },
                success: function (data) {
                  $(btn).parents('.' + prefix).remove();
                },
                type: 'GET'
            });
          }else{
            $(btn).parents('.' + prefix).remove();
          }

          var forms = $('.' + prefix); // Get all the forms
          // Update the total number of forms (1 less than before)
          $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
          var i = 0;
          // Go through the forms and set their indices, names and IDs
          for (formCount = forms.length; i < formCount; i++) {
              $(forms.get(i)).find('.formset-field').each(function () {
                  updateElementIndex(this, prefix, i);
              });
          }
      } // End if

      return false;
  }



  $("body").on('click', '.remove-form-row',function () {
    return deleteForm($(this), String($(this).attr('id')));
  });

  $("body").on('click', '.add-form-row',function () {
      return addForm($(this), String($(this).attr('id')));
  });

