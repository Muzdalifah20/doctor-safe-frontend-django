document.addEventListener('DOMContentLoaded', () => {
  const dropdownBtn = document.getElementById('userDropdownBtn');
  const dropdownContent = document.getElementById('userDropdown');

  dropdownBtn.addEventListener('click', () => {
    dropdownContent.classList.toggle('dropdown-active');
  });

  // Close the dropdown if clicked outside
  document.addEventListener('click', (event) => {
    if (!dropdownBtn.contains(event.target) && !dropdownContent.contains(event.target)) {
      dropdownContent.classList.remove('dropdown-active');
    }
  });
});
