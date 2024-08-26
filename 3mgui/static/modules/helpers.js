var apiurl = 'http://127.0.0.1:8000'
var test = [{"one":"1", "two":"2"},{"one":"4", "two":"5"}]

async function sendGet(){
    //fillTable(test) //Test data
    wipeTable()
    var callurl = apiurl + '/getall'
    const response = await fetch(callurl,
    {
       "method": "GET"
    })

    if (!response.ok) {
        const message = `An error has occured: ${response.status}`
        throw new Error(message)
    }

    const data = await response.json()
    fillTable(data)

    return data
}

async function sendPost(){
    wipeTable()
    var callurl = apiurl + '/update'
    var payload_json = {
        "lucky_num": document.getElementById('lnum_input').value,
        "guest_ip": document.getElementById('client_ip').innerHTML
        }
    fetch(callurl, {
        "method": "POST",
        "headers": { 'Content-Type':'application/json'},
        "body": JSON.stringify(payload_json)
    })
    .then(response => response.json())
    .then(data => {
        sendGet()
        console.log(data)
    })
    .catch(err => alert(err));

}

function fillTable(data){
    var datatbl = document.getElementById('display_table')
    //Make header row from keys in the first item
    var headrow = document.createElement('tr')
    for (var key in data[0]){
        var newth = document.createElement('th')
        newth.appendChild(document.createTextNode(key))
        headrow.appendChild(newth)
    }
    datatbl.appendChild(headrow)

    //Fill out table with rest of the values
    for (var i=0; i < data.length; i++){
        var newtr = document.createElement('tr')
        var item = data[i]
        for (var key in item){
            var newtd = document.createElement('td')
            var value = item[key]
            newtd.appendChild(document.createTextNode(value))
            newtr.appendChild(newtd)
        }
        datatbl.appendChild(newtr)
    }
}

function wipeTable(){
    document.querySelectorAll("tr").forEach(function(node) {
        node.remove()
    })
}

//fillTable(test)
//sendGet()