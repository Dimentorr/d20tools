const character_lvl = document.getElementById("character_lvl");

character_lvl.addEventListener('change', function(event)
{
    let all_classes = document.querySelectorAll('[name="lvl_class"]');
    for (let i = 0; i < all_classes.length; ++i) {
        let item = all_classes[i];
        item.max = character_lvl.value;
    }
});
