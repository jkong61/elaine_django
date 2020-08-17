const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const inspectionSelector = document.getElementById('id_model_select');
const instanceSelector = document.getElementById('id_instance_select');
const dateStart = document.getElementById('id_validity_start_date');
const dateEnd = document.getElementById('id_validity_end_date');
const calculateDate = document.getElementById('id_date_calculate');

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

calculateDate.onclick = () =>
{
    if(inspectionSelector.value)
    {
        switch(inspectionSelector.value)
        {
            case("skv"):
            case("slv"):
                dateEnd.value = addDays(dateStart.value, 183).toLocaleDateString();
                break;
            case("pwmaj"):
                dateEnd.value = addDays(dateStart.value, 365.25 * 5).toLocaleDateString();
                break;
            case("pwppj"):
                dateEnd.value = addDays(dateStart.value, 91).toLocaleDateString();
                break;
            default:
                dateEnd.value = addDays(dateStart.value, 365.25).toLocaleDateString();
        }
    }
    else
    {
        alert("Please select an inspection type.");
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