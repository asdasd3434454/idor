window.onload = function () {
  const urlParams = new URLSearchParams(window.location.search);
  const userId = urlParams.get('id');

  fetch('users.json')
    .then(response => response.json())
    .then(data => {
      if (data[userId]) {
        document.getElementById("result").innerText = "🎉 You won!";
      } else {
        document.getElementById("result").innerText = "❌ Try harder!";
      }
    })
    .catch(err => {
      document.getElementById("result").innerText = "Error loading user data.";
      console.error(err);
    });
};
