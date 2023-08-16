showList();

function showList(){
	console.log(postes);
	postes = JSON.parse(postes);
	const $div = $(".board-list");
	let text = "";


	postes.forEach(post => {
		text += `
			<div class="post">
				<div class="checkbox"><input type="checkbox" name="postId" value="${post.postId}"></div>
				<div class="post-id">${post.postId}</div>
				<div class="post-type">${post.postType}</div>
				<div class="post-name">${post.postName}</div>
				<div class="post-content">${post.postContent}</div>
				<div class="post-register-date">${post.postRegisterDate}</div>
				<div class="member-id">${post.memberId}</div>
				<div class="post-is-blinded">${post.postIsBlinded}</div>
			</div>
			`;
	});
	
	$div.append(text);
	
}

$(document).ready(function() {
    $('input[type=checkbox]').change(function() {
        if (this.checked) {
            alert(`${this.value} is checked`);
        }
        else {
            alert(`${this.value} is unchecked`);
        }
    });
});

$('.button-delete').click(function(){
	if($("input:checkbox:checked").length === 0){
		alert("삭제할 항목을 선택해 주세요.");
		return;
	}
	
	var checkedPosts = [];
  $("input:checkbox:checked").each(function(){
    checkedPosts.push($(this).val());
  });

  // AJAX 요청
  $.ajax({
    type: "post",
    url: "/delete.post",
    data: { posts: checkedPosts },
    dataType: "json",
    success: function(response){
      if (response.success) {
        alert("게시글이 삭제되었습니다.");
        window.location.reload();
      } else {
        alert("게시글 삭제에 실패했습니다.");
      }
    }
  });
	
});

