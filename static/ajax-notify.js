function ajaxpost () {
  // (A) GET FORM DATA
  var data = new FormData(document.getElementById("myForm"));

  // (B) AJAX REQUEST
  // (B1) POST DATA TO SERVER, RETURN RESPONSE AS TEXT
  fetch("abewoycke.pythonanywhere.com/view_poll_results", { method:"POST", body:data })
  .then(res => res.text())

  // (B2) SHOW MESSAGE ON SERVER RESPONSE
  .then(response => {
    console.log(response);})

  // (B3) OPTIONAL - HANDLE FETCH ERROR
  .catch(err => console.error(err));

  // (C) PREVENT FORM SUBMIT
  return false;
}