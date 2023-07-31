let alertremove = document.querySelectorAll('.alert')
alertremove.forEach(element => {
    setTimeout(() => {
        
        element.remove()
    }, 2000);
    
});