const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const inspectionSelector = document.getElementById('id_model_select');
const instanceSelector = document.getElementById('id_instance_select');
const dateStart = document.getElementById('id_validity_start_date');
const dateEnd = document.getElementById('id_validity_end_date');

window.onload = () =>
{
    dateStart.value = new Date().toLocaleDateString();
    inspectionSelector.value = ''
};

inspectionSelector.onchange = () =>
{
    if(inspectionSelector.value)
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
            body: JSON.stringify({'data' : inspectionSelector.value})
        })
        .then(response => response.json())
        .then(data => populate_select(instanceSelector,data))
        .catch(error =>console.log(error))
    }
    else
    {
        removeOptions(instanceSelector)
    }
};

dateStart.onchange = () =>
{
    if(inspectionSelector.value == 'skv' && inspectionSelector.value == 'slv')
    {
        dateEnd.value = addDays(new Date(), 365)
    }
};

function populate_select(selectElement, data)
{
    removeOptions(selectElement);
    array = data.data
    for(i = 0; i < array.length; i++)
    {
        var option = document.createElement('option');
        option.value = array[i].id;
        option.text = array[i].str;
        selectElement.add(option)
    }
};

function removeOptions(selectElement) 
{
    var i, L = selectElement.options.length - 1;
    for(i = L; i >= 0; i--) {
       selectElement.remove(i);
    }
};

function addDays(date, days) 
{
    var result = new Date(date);
    result.setDate(result.getDate() + days);
    return result;
}