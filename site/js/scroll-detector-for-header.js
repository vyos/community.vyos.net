document.addEventListener('DOMContentLoaded', function () {
  resolveHeadersClasses()

  document.addEventListener('scroll', () => {
    resolveHeadersClasses()
  })
})

function resolveHeadersClasses() {
  const header = document.getElementById('navigation')
  const background = 'background__white'
  const shadow = 'bottom-shadow'

  if(!header) return

  if(window?.scrollY && window.scrollY > 0) {
    if(header.classList.contains(background)) return

    header.classList.add(background)
    header.classList.add(shadow)
  } else {
    if(!header.classList.contains(background)) return

    header.classList.remove(background)
    header.classList.remove(shadow)
  }
}