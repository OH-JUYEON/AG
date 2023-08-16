/**
 * 
 */

showList();

function showList(){
	console.log(KHC);
	KHC = JSON.parse(KHC);
	//files = JSON.parse(files);
	const $ul = $("#content-wrap ul");
	let text = "";
	
	KHC.forEach(board => {
		text += `
				<li class="pro-knowhow-list-item" >
					<section class="item-wrapper">
						<a href="master-know-how-free-detail.jsp">								<figure class="image-wrapper">
							<img
								src="https://static.cdn.soomgo.com/upload/talkboard/f075fba9-b4bd-4611-b21b-3dfda78f4c05.jpg?webp=1"
									class="content-image">
								</figure>
							<h3 class="content-title">'시간 가는 줄 모르는 수업' 만드는 고수</h3>										<p class="content-writer">권지안</p>
						</a>
					</section>
				</li>
						
			`;
	});
	
	if(KHC.length == 0){
		text += `
			<li>
		        <div>
					현재 게시글이 없습니다. 게시글 작성을 해보세요!
				</div>
			</li>
		`
	}
	
	$ul.append(text);
}














