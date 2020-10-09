
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
            // Clone a form (without event handlers) from the first form
            var row = $(".education:last").clone(false).get(0);

            // Insert it after the last form
            $(row).removeAttr('id').hide().insertAfter(".education:last").slideDown(30);

            // Remove the bits we don't want in the new row/form
            // e.g. error messages
            $(".errorlist", row).remove();
            $(row).children().removeClass("error");

            // Relabel or rename all the relevant bits
            $(row).find('.form-control').each(function () {
                updateElementIndex(this, prefix, formCount);
                $(this).val('');
                $(this).removeAttr('value');
                $(this).prop('checked', false);
            });

            // Add an event handler for the delete education/form link
            $(row).find(".delete").click(function () {
                return deleteForm(this, prefix);
            });
            // Update the total form count
            $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);

        } // End if
     }else if(prefix == 'experienceInfo'){
         if (formCount < 1000) {
            // Clone a form (without event handlers) from the first form
            var row = $(".experience:last").clone(false).get(0);

            // Insert it after the last form
            $(row).removeAttr('id').hide().insertAfter(".experience:last").slideDown(30);

            // Remove the bits we don't want in the new row/form
            // e.g. error messages
            $(".errorlist", row).remove();
            $(row).children().removeClass("error");

            // Relabel or rename all the relevant bits
            $(row).find('.form-control').each(function () {
                updateElementIndex(this, prefix, formCount);
                $(this).val('');
                $(this).removeAttr('value');
                $(this).prop('checked', false);
            });

            // Add an event handler for the delete education/form link
            $(row).find(".delete").click(function () {
                return deleteForm(this, prefix);
            });
            // Update the total form count
            $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);

        } // End if
     } else if(prefix == 'skills'){
      if (formCount < 1000) {
            // Clone a form (without event handlers) from the first form
            var row = $(".skill:last").clone(false).get(0);
            $(row).removeAttr('id').hide().insertAfter(".skill:last").slideDown(30);

            // Remove the bits we don't want in the new row/form
            // e.g. error messages
            $(".errorlist", row).remove();
            $(row).children().removeClass("error");

            // Relabel or rename all the relevant bits
            $(row).find('.form-control').each(function () {
                updateElementIndex(this, prefix, formCount);
                $(this).val('');
                $(this).removeAttr('value');
                $(this).prop('checked', false);
            });

            // Add an event handler for the delete education/form link
            $(row).find(".delete").click(function () {
                return deleteForm(this, prefix);
            });
            // Update the total form count
            $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);

        } // End if
     }else if(prefix == 'certificate'){
        if (formCount < 1000) {
            // Clone a form (without event handlers) from the first form
           var row = $(".certificate:last").clone(false).get(0);
            $(row).removeAttr('id').hide().insertAfter(".certificate:last").slideDown(30);
            // Remove the bits we don't want in the new row/form
            // e.g. error messages
            $(".errorlist", row).remove();
            $(row).children().removeClass("error");

            // Relabel or rename all the relevant bits
            $(row).find('.form-control').each(function () {
                updateElementIndex(this, prefix, formCount);
                $(this).val('');
                $(this).removeAttr('value');
                $(this).prop('checked', false);
            });

            // Add an event handler for the delete education/form link
            $(row).find(".delete").click(function () {
                return deleteForm(this, prefix);
            });
            // Update the total form count
            $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);

        } // End if
     }else if(prefix == 'language'){
      if (formCount < 1000) {
            // Clone a form (without event handlers) from the first form
    var row = $(".language:last").clone(false).get(0);
            $(row).removeAttr('id').hide().insertAfter(".language:last").slideDown(30);
            // Remove the bits we don't want in the new row/form
            // e.g. error messages
            $(".errorlist", row).remove();
            $(row).children().removeClass("error");

            // Relabel or rename all the relevant bits
            $(row).find('.form-control').each(function () {
                updateElementIndex(this, prefix, formCount);
                $(this).val('');
                $(this).removeAttr('value');
                $(this).prop('checked', false);
            });

            // Add an event handler for the delete education/form link
            $(row).find(".delete").click(function () {
                return deleteForm(this, prefix);
            });
            // Update the total form count
            $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);

        } // End if
     }else if(prefix == 'other'){
      if (formCount < 1000) {
            // Clone a form (without event handlers) from the first form
     var row = $(".others:last").clone(false).get(0);
            $(row).removeAttr('id').hide().insertAfter(".others:last").slideDown(30);
            // Remove the bits we don't want in the new row/form
            // e.g. error messages
            $(".errorlist", row).remove();
            $(row).children().removeClass("error");

            // Relabel or rename all the relevant bits
            $(row).find('.form-control').each(function () {
                updateElementIndex(this, prefix, formCount);
                $(this).val('');
                $(this).removeAttr('value');
                $(this).prop('checked', false);
            });

            // Add an event handler for the delete education/form link
            $(row).find(".delete").click(function () {
                return deleteForm(this, prefix);
            });
            // Update the total form count
            $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1);

        } // End if
        }
    return false;
}


function deleteForm(btn, prefix) {

console.log(prefix)
      var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
       if(prefix == 'educationalInfo'){
            if (formCount > 1) {
          // Delete the education/form
          var goto_id = $(btn).find('input').val();
          if( goto_id ){
            $.ajax({
                url: "/" + window.location.pathname.split("/")[1] + "/formset-data-delete/"+ goto_id +"/?next="+ window.location.pathname,
                error: function () {
                  console.log("error");
                },
                success: function (data) {
                  $(btn).parents('.education').remove();
                },
                type: 'GET'
            });
          }else{
            $(btn).parents('.education').remove();
          }

          var forms = $('.education'); // Get all the forms
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
       }else if(prefix == 'experienceInfo'){
            if (formCount > 1) {
          // Delete the education/form
          var goto_id = $(btn).find('input').val();
          if( goto_id ){
            $.ajax({
                url: "/" + window.location.pathname.split("/")[1] + "/formset-data-delete/"+ goto_id +"/?next="+ window.location.pathname,
                error: function () {
                  console.log("error");
                },
                success: function (data) {
                  $(btn).parents('.experience').remove();
                },
                type: 'GET'
            });
          }else{
            $(btn).parents('.experience').remove();
          }

          var forms = $('.experience'); // Get all the forms
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
      } else if(prefix == 'skills'){
       if (formCount > 1) {
          // Delete the education/form
          var goto_id = $(btn).find('input').val();
          if( goto_id ){
            $.ajax({
                url: "/" + window.location.pathname.split("/")[1] + "/formset-data-delete/"+ goto_id +"/?next="+ window.location.pathname,
                error: function () {
                  console.log("error");
                },
                success: function (data) {
                  $(btn).parents('.skill').remove();
                },
                type: 'GET'
            });
          }else{
            $(btn).parents('.skill').remove();
          }

          var forms = $('.skill'); // Get all the forms
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
      }else if(prefix == 'certificate'){
       if (formCount > 1) {
          // Delete the education/form
          var goto_id = $(btn).find('input').val();
          if( goto_id ){
            $.ajax({
                url: "/" + window.location.pathname.split("/")[1] + "/formset-data-delete/"+ goto_id +"/?next="+ window.location.pathname,
                error: function () {
                  console.log("error");
                },
                success: function (data) {
                  $(btn).parents('.certificate').remove();
                },
                type: 'GET'
            });
          }else{
            $(btn).parents('.certificate').remove();
          }

          var forms = $('.certificate'); // Get all the forms
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
      }else if(prefix == 'language'){
       if (formCount > 1) {
          // Delete the education/form
          var goto_id = $(btn).find('input').val();
          if( goto_id ){
            $.ajax({
                url: "/" + window.location.pathname.split("/")[1] + "/formset-data-delete/"+ goto_id +"/?next="+ window.location.pathname,
                error: function () {
                  console.log("error");
                },
                success: function (data) {
                  $(btn).parents('.language').remove();
                },
                type: 'GET'
            });
          }else{
            $(btn).parents('.language').remove();
          }

          var forms = $('.language'); // Get all the forms
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
      }else if(prefix == 'other'){
       if (formCount > 1) {
          // Delete the education/form
          var goto_id = $(btn).find('input').val();
          if( goto_id ){
            $.ajax({
                url: "/" + window.location.pathname.split("/")[1] + "/formset-data-delete/"+ goto_id +"/?next="+ window.location.pathname,
                error: function () {
                  console.log("error");
                },
                success: function (data) {
                  $(btn).parents('.others').remove();
                },
                type: 'GET'
            });
          }else{
            $(btn).parents('.others').remove();
          }

          var forms = $('.others'); // Get all the forms
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
      }
      return false;
  }

  $("body").on('click', '.remove-form-row',function () {
      return deleteForm($(this), String($(this).attr('id')));
  });

  $("body").on('click', '.add-form-row',function () {
      return addForm($(this), String($(this).attr('id')));
  });

