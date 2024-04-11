document.addEventListener('DOMContentLoaded', function (event) {
	const canvas = document.getElementById('canvas')
  if(event?.target?.body?.clientWidth > 575) {
    const r = new rive.Rive({
      src: '/img/banner-bubbles.riv',
      canvas: document.getElementById('canvas'),
      autoplay: true,
      stateMachines: 'State Machine 1',
      onLoad: () => {
        r.resizeDrawingSurfaceToCanvas()
      },
    })

    canvas.classList.add('canvas-present')
  }

	addEventListener('resize', (e) => {
		if (!e?.currentTarget?.innerWidth) return

		if (Number(e?.currentTarget?.innerWidth) > 575) {
      if(canvas.classList.contains('canvas-present')) {
        return
      }
      
			canvas.classList.remove('not_visible')
			canvas.classList.add('canvas-present')
      const r = new rive.Rive({
				src: '/img/banner-bubbles.riv',
				canvas: document.getElementById('canvas'),
				autoplay: true,
				stateMachines: 'State Machine 1',
				onLoad: () => {
					r.resizeDrawingSurfaceToCanvas()
				},
			})
		} else {
			canvas.classList.add('not_visible')
		}
	})
})
