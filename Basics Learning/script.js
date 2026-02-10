let loadbtn = document.getElementById("loadBtn");
let userlist = document.getElementById("userList");

loadbtn.addEventListener("click", async function () {

  let response = await fetch("https://jsonplaceholder.typicode.com/users");
  let data = await response.json();

  data.forEach(user => {
    let li = document.createElement("li");
    li.innerText = user.name;
    userlist.appendChild(li);
  });
});
