function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const CSRF_TOKEN = getCookie("csrftoken");

// standard function for sending requests

async function sendRequest(endpoint, options) {
  let _status = -1;
  try {
    const response = await fetch(endpoint, options);
    _status = response.status;
    if (response.status >= 500) {
      throw new Error("Network response was not ok");
    }
    const _data = await response.json();
    return {
      data: _data,
      status: _status,
    };
  } catch (error) {
    return {
      status: _status,
      data: error,
    };
  }
}
