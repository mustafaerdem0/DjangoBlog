let form = document.querySelectorAll("#form input,textarea,input")
form.forEach((element)=>{
    element.classList.add('form-control')

})
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');

    checkboxes.forEach(checkbox => {
        checkbox.classList.add('form-check-input');
    });

