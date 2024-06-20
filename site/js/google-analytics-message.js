document.addEventListener('DOMContentLoaded', function (event) {

  function determineDataOfExpiration() {
    const date = new Date();
    date.setMonth(date.getMonth() + 1);  // Add one month to the current date
    const expiresString = "expires=" + date.toUTCString()
    return expiresString
  }
	// function to toggle Google Analytics message
  const toggleGoogleAnalyticsMessage = action => {
    const message = document.getElementById('google-analytics-message')
    action === 'show' && message.classList.add('open')
    action === 'hide' && message.classList.remove('open')
  }

  // check if cookies with user choice exist
  const isGoogleAnalyticsAllowedValueExist =
    document.cookie.split(';')
      .find(row => row.includes('isGoogleAnalyticsAllowed'))

  // if the user has already made a choice
  if (isGoogleAnalyticsAllowedValueExist) {

    const isGoogleAnalyticsAllowedValue = isGoogleAnalyticsAllowedValueExist.split('=')[1]

    // and if the user chose "Accept" - connect Google Analytics
    if (isGoogleAnalyticsAllowedValue === 'yes') {
      window.dataLayer = window.dataLayer || [];
      function gtag() { dataLayer.push(arguments); }
      gtag('js', new Date());
      gtag('config', 'G-J3WHFQG00P');
    }

  } else {

    // display a message with a question
    toggleGoogleAnalyticsMessage('show')

    const googleAnalyticsMessageAccept = document.querySelector('#google-analytics-accept')
    const googleAnalyticsMessageDecline = document.querySelectorAll('#google-analytics-decline')

    // register a click on the "Accept" button
    googleAnalyticsMessageAccept.addEventListener('click', function () {
      document.cookie = `isGoogleAnalyticsAllowed=yes;${determineDataOfExpiration()};path=/`
      toggleGoogleAnalyticsMessage('hide')
    })

    // register a click on the "Decline" button
    googleAnalyticsMessageDecline.forEach(el => {
      el.addEventListener('click', function () {
        document.cookie = `isGoogleAnalyticsAllowed=no;${determineDataOfExpiration()};path=/`
        toggleGoogleAnalyticsMessage('hide')
      })
    })

  }
})