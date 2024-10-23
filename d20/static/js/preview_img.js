document.getElementById('image-upload').addEventListener('change', function(event) {
  const file = event.target.files[0]; // Получить выбранный файл
  if (file) {
    const reader = new FileReader(); // Создать объект FileReader

    reader.onload = function(event) {
      document.getElementById('image-preview').src = event.target.result;
    }

    reader.readAsDataURL(file); // Прочитать файл как Data URL
  } else {
    document.getElementById('image-preview').src = "#"; // Сбросить превью
  }
});