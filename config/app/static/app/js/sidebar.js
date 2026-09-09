const aside = document.querySelector('.aside_component');
const mainContainer = document.querySelector('.main_container');

console.log('ASIDE:', aside);
console.log('MAIN:', mainContainer);

aside.addEventListener('click', async (event) => {

    const item = event.target.closest('.menu_tile');

    if (!item) return;

    const page = item.dataset.page;

    if (!page) {
        console.warn('Esta tile no tiene data-page');
        return;
    }

    console.log('Clicked:', page);

    try {

        console.log('1️⃣ Haciendo fetch...');

        const response = await fetch(page);

        console.log('2️⃣ Response:', response);
        console.log('3️⃣ Status:', response.status);
        console.log('4️⃣ OK:', response.ok);
        console.log('5️⃣ URL final:', response.url);

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const html = await response.text();

        console.log('6️⃣ HTML recibido:', html);
        console.log('7️⃣ HTML length:', html.length);

        mainContainer.innerHTML = html;

        console.log('8️⃣ HTML insertado');

        document.querySelectorAll('.menu_tile').forEach(menu => {
            menu.classList.remove('active');
        });

        item.classList.add('active');

        console.log('9️⃣ Tile activada');

    } catch (error) {

        console.error('💀 ERROR:', error);

    }

});