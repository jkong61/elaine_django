const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const selector = document.getElementById('id_test_select')
selector.onchange = () =>
{
    fetch('/inspections/api/', {
            method : 'POST',
            credentials: 'same-origin',
            headers: 
            {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
            },
            mode: 'same-origin',
            body: JSON.stringify({'data' : selector.value})
        })
    .then(response => response.json())
    .then(data => 
        {
            console.log(data)
        })
};