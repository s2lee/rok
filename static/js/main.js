function checkbox1() {
  var body = $("body");

  if ($("#customer-check").is(':checked')) {
      $("#customer-check").prop("checked", false);
      if ($("#check").is(':checked')){
        body.css('overflow-y','hidden');

      } else {
        body.css('overflow-y','auto');
      }
  } else {
    if ($("#check").is(':checked')){
      body.css('overflow-y','hidden');

    } else {
      body.css('overflow-y','auto');
    };
  };
};

function checkbox2() {
  var body = $("body");

  if ($("#check").is(':checked')) {
      $("#check").prop("checked", false);
      if ($("#customer-check").is(':checked')){
        body.css('overflow-y','hidden');

      } else {
        body.css('overflow-y','auto');
      }
  } else {
    if ($("#customer-check").is(':checked')){
      body.css('overflow-y','hidden');

    } else {
      body.css('overflow-y','auto');
    };
  };
};


window.addEventListener("scroll", function(){
  var top = document.querySelector(".top");
  var logo = document.querySelector(".logo");
  var userNav = document.querySelector(".user-nav-links");
  var logoContainer = document.querySelector(".logo-container");
  var navbtn = document.querySelector(".nav-btn");
  var customerNavbtn = document.querySelector(".customer-nav-btn");
  top.classList.toggle("disapear", window.scrollY > 0);
  logo.classList.toggle("style-logo-scrolled", window.scrollY > 0);
  userNav.classList.toggle("style-usernav-scrolled", window.scrollY > 0);
  logoContainer.classList.toggle("style-logo-container-scrolled", window.scrollY > 0);
  navbtn.classList.toggle("style-navbar-scrolled", window.scrollY > 0);
  customerNavbtn.classList.toggle("style-customerNavbar-scrolled", window.scrollY > 0);
})

$(window).on("scroll",function() {
  var navbtn = $(".nav-btn");
  var cusnavbtn = $(".customer-nav-btn");
  var header = $("header");

  if($(window).scrollTop() > 0 ) {
    navbtn.css('top','2.5rem');
    cusnavbtn.css('top','2.5rem');
    header.css('top','0');

  } else {
    navbtn.css('top','4.5rem');
    cusnavbtn.css('top','4.5rem');
    header.css('top','32px');
  }

});


$(".carousel").owlCarousel({
  autoWidth:true,
  margin: 30,
  dots: false,
  responsive:{
    0:{
      items: 1,
      center:true,

    },
    600:{
      items: 2,

    },
    1000:{
      items: 3,

    }
  }
});

function truncateText(selector, maxLength) {
  $(selector).text((i, txt) => txt.length > maxLength ? txt.substr(0,maxLength) + "..." : txt);
};
truncateText(".top-article-contents", 90);
truncateText(".top-article-contents-mobile", 110);


const tabcontents = document.querySelectorAll(".tabcontent");
const tabLinks = document.querySelectorAll(".tabs a");

function openTab(event, tabName) {
  tabcontents.forEach((tabcontent) => (tabcontent.style.display = "none"));

  tabLinks.forEach((tabLink) => tabLink.classList.remove("tab-active"));

  event.currentTarget.classList.add("tab-active");
  document.getElementById(tabName).style.display = "block";
}

window.addEventListener( "pageshow", function ( event ) {
  var historyTraversal = event.persisted ||
                         ( typeof window.performance != "undefined" &&
                              window.performance.navigation.type === 2 );
  if ( historyTraversal ) {
    // Handle page restore.
    window.location.reload();
  }
});
