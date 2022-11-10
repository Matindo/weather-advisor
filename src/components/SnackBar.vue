<template>
  <div id="snackbar">{{ message }}</div>
</template>

<script>
export default {
  name: 'SnackBar',
  props: {
    message: {
      type: String,
      required: true
    },
    variant: {
      type: String,
      required: true
    }
  },
  created: function () {
    const snackbar = document.getElementById('snackbar')
    if ((this.variant === 'warning') || (this.variant === 'light')) { snackbar.style.color = '#343a40' }
    if (this.variant === 'success') {
      snackbar.style.backgroundColor = '#28a745'
    } else if (this.variant === 'dark') {
      snackbar.style.backgroundColor = '#343a40'
    } else if (this.variant === 'info') {
      snackbar.style.backgroundColor = '#17a2b8'
    } else if (this.variant === 'warning') {
      snackbar.style.backgroundColor = '#ffc107'
    } else if (this.variant === 'danger') {
      snackbar.style.backgroundColor = '#dc3545'
    } else if (this.variant === 'primary') {
      snackbar.style.backgroundColor = '#007bff'
    } else if (this.variant === 'secondary') {
      snackbar.style.backgroundColor = '#6c757d'
    } else if (this.variant === 'light') {
      snackbar.style.backgroundColor = 'f8f9fa'
    }
  },
  mounted: function () {
    setTimeout(function () { document.getElementById('snackbar').className = document.getElementById('snackbar').className.replace('show', '') }, 5000)
  }
}
</script>

<style lang="scss" scoped>
#snackbar {
  visibility: hidden; /* Hidden by default. Visible on click */
  min-width: 250px; /* Set a default minimum width */
  margin-left: -125px; /* Divide value of min-width by 2 */
  color: #f8f9fa; /* white text color */
  text-align: center; /* Centered text */
  border-radius: 2px; /* Rounded borders */
  padding: 16px; /* Padding */
  position: fixed; /* Sit on top of the screen */
  z-index: 1; /* Add a z-index if needed */
  left: 50%; /* Center the snackbar */
  bottom: 30px; /* 30px from the bottom */
  &.show {
    visibility: visible;
    -webkit-animation: fadein 0.5s, fadeout 0.5s 2.5s;
    animation: fadein 0.5s, fadeout 0.5s 2.5s;
  }
}

@-webkit-keyframes fadein {
  from {bottom: 0; opacity: 0;}
  to {bottom: 30px; opacity: 1;}
}

@keyframes fadein {
  from {bottom: 0; opacity: 0;}
  to {bottom: 30px; opacity: 1;}
}

@-webkit-keyframes fadeout {
  from {bottom: 30px; opacity: 1;}
  to {bottom: 0; opacity: 0;}
}

@keyframes fadeout {
  from {bottom: 30px; opacity: 1;}
  to {bottom: 0; opacity: 0;}
}
</style>
