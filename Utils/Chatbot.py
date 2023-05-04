import requests
import random

def requests_api(question):
    return requests.post("https://api.simsimi.vn/v2/simtalk", headers = {"Content-Type": "application/x-www-form-urlencoded"}, data = {"text": f"{question}", "lc": "vn"}).json()["message"]

def ChatBot(question:str):
    data = requests_api(question)
    list = [
        "lồn",
        "địt",
        "cặc",
        "đụ",
        "bố"
        "cút"
    ]
    
    list_warn = [
        "cô đơn",
        "buồn",
        "mệt",
        "stress",
        "nhọc",
        "chán",
    ]
    
    list_danger = [
        "cứu",
        "giúp",
        "bạo",
        "hiếp",
        "dâm",
        "cưỡng",
        "hiếp",
        "đập"
    ]

    list_SOS = [
        "cứu",
        "giúp",
        "đau",
        "đánh",
        "đập",
        "hạ",
        "tự tử",
        "tự sát",
        "tự giết",
        "tự vẫn",
        "kết thúc",
        "chết",
        "tử vong",
        "sống"
    ]

    emoji = [
        "😂","😁","😀","😃","😄","😅","😆","😉","😊","😋","😎","😍","😘","😗","😙","😚","☺️","🙂","🤗","🤔","😐","😑","😶","🗿","😏","😣","😥","😮","🤐","😯","😪","😫","😴","😌","😛","😜","😝","🤤","😒","😓","😔","😕","🙃","🤑","😲","☹️","🙁","😖","😞","😟","😤","😢","😭",
    ]
    Kaomoji = [
        "( ͡° ͜ʖ ͡°)",
        "╰(*°▽°*)╯",
        "(´｡• ᵕ •｡`)",
        "(´｡• ω •｡`)",
        "(´｡• ᵕ •｡`)",
        "(´｡• ᵕ ^｡`)",
        "(´｡• ω •｡`)",
        "(´｡• ω •｡`)",
        "(┬┬﹏┬┬)",
        "(°▽°)",
        "(*/ω＼*)",
        "（〃｀ 3′〃）",
        "( ´･･)ﾉ(._.`)",
        "(╯°□°）╯︵ ┻━┻",
        "༼ つ ◕_◕ ༽つ",
        "¯\_(ツ)_/¯",
        "ಠ_ಠ",
        "ಥ_ಥ",
        "ಥ﹏ಥ",
        "（；へ：）",
        "(￣ヘ￣)",
        "ヽ(´□｀。)ﾉ",
        "ヽ(`Д´)ﾉ",
        "ヽ(｀⌒´メ)ノ"
    ]
    
    check_list = [
        "True",
        "False"
    ]
    
    warn = False
    danger = False
    SOS = False

    data_reply_warn=[
        "Nếu cậu có việc gì khó nói thì cứ nói với tớ nhé, tớ sẽ giúp cậu.",
        "Nếu cậu bị bạo lực học đường thì đừng sợ hãy cứ nói ra",
        "Nếu cậu thực sự cần 1 người để nói chuyện hãy thử báo với 111 -  Tổng đài điện thoại Quốc gia bảo vệ trẻ em",
        "Nếu cậu thực sự cần 1 người để nói chuyện hãy thử báo với 18001567 - Tổng đài hỗ trợ tâm lý",
        "Nếu cậu cảm thấy quá mệt mỏi với việc học tập thì cứ nằm nghỉ ngơi 1 chút đi nhé,tuy đơn giản nhưng nó sẽ giúp cậu tốt hơn rất nhiều đấy",
        "Đừng sợ việc phải nói ra! Hãy nói ra điều đó đi nhé! Nó sẽ giúp cậu tốt hơn rất nhiều đấy",
        "Nếu thực sự quá mệt mỏi hãy nghỉ ngơi 1 chút đi nhé!Không sao đâu",
        "Hãy nằm xuống và hãy thử lắng nghe 1 bài nhạc đi nhé! Nó sẽ giúp cậu tốt hơn rất nhiều đấy Ngày mai cậu sẽ cảm thấy tốt hơn thôi",
        "Đừng phải quá cố gắng gì cả!Hãy nghỉ ngơi 1 chút đi nhé! Ngày mai sẽ tốt hơn thôi",
        "Hãy thử nghỉ ngơi 1 chút đi nhé! Ngày mai cậu sẽ cảm thấy tốt hơn thôi",
        "Hãy đeo thử tai nghe và chìm sâu lắng nghe 1 bài hát đi nhé! Ngày mai cậu sẽ cảm thấy tốt hơn thôi",
    ]
    
    data_reply_darnger=[
        "Đừng sợ! Có tui đây rồi",
        "Cậu càng cố gắng thì càng khó khăn hơn đấy! Hãy thử nghỉ ngơi 1 chút đi nhé!",
        "Nếu cậu làm bất cứ việc gì!Ngoài những người quan tâm đến cậu đau lòng ra thì ns cx sẽ chả giải quyết được gì",
        "Đừng im lặng! don't be silent - Im lặng là thứ tệ nhất mà cậu có thể làm",
        "Hãy bỏ những việc cậu đang làm lại và nghỉ ngơi 1 chút đi nhé! Ngày mai cậu sẽ cảm thấy tốt hơn thôi",
        "Dù cho mai về sau,nhất định mọi việc sẽ tốt hơn thôi",
        "Hãy thử nghỉ ngơi 1 chút đi nhé! Ngày mai cậu sẽ cảm thấy tốt hơn thôi",
        "Hãy đeo thử tai nghe và chìm sâu lắng nghe 1 bài hát đi nhé! Ngày mai cậu sẽ cảm thấy tốt hơn thôi",
        "Ai cx từng trải qua những khó khăn như cậu đấy! Hãy thử nghỉ ngơi 1 chút đi nhé! Ngày mai cậu sẽ cảm thấy tốt hơn thôi",
        "Trưởng thành tí nào cậu bé, cậu sẽ vượt qua được mọi khó khăn thôi",
        "Ăn miếng bánh, trả miếng bánh! Cậu sẽ vượt qua được mọi khó khăn thôi",
        "Đừng im lặng - Im lặng là thứ tệ nhất mà cậu có thể làm",
        "Bỏ hết những việc cậu đang làm,hít thở 1 hơi thật sâu và nghỉ ngơi 1 chút đi nhé! Ngày mai cậu sẽ cảm thấy tốt hơn thôi",
    ]

    data_reply_SOS=[
        "Này cậu, trước tiên cậu hãy bình tĩnh lại. Tớ biết lúc này cậu đang cảm thấy rất cô độc, không còn ai hiểu cậu, tâm trạng và cảm xúc hổn loạn, rối bời. Nhưng vẫn có tớ ở đây với cậu, tớ nghĩ rằng đâu đó trong cuộc sống của cuộc vẫn còn chút ánh sáng, cuộc sống của cậu còn nhiều điều tốt đẹp khác mà cậu chưa được trải nghiệm. Và niềm tin vào cuộc sống này là liều thuốc an toàn nhất.",
        "Nếu cậu cảm thấy nguy hiểm ngay trong chính ngôi nhà của mình hãy báo 113 ngay nhé!",
        "Hy vọng là điều vô nghĩa khi khủng hoảng xảy ra, nhưng điều tốt nhất lúc này cậu có thể làm là cho mình thêm 24h và cố gắng nghĩ rằng suy nghĩ đó của bản thân chỉ là nhất thời mà thôi.",
        "Những chuyện vừa qua đã giúp chúng ta hiểu rõ hơn về thế giới bên ngoài, về lòng người. Nhưng chúng ta có thể sẽ vẫn đi lại và hít thở bầu không khí trong lành. Hãy nghĩ đến những bệnh nhân ung thư- những người kháo khát được sống đến nhường nào. Vì thế câu cần trân trọng cuộc sống này hơn",
        " Hãy hướng về tương lai tốt đẹp, mọi phiền muộn của quá khứ hãy bỏ lại sau lưng.",
        "Tôi không thể khiến những đau khổ của bạn tan biến, cũng không thể dự đoán những điều trong tương lai nhưng tôi biết bạn sẽ đủ niềm tin và nghị lực để vượt qua.",
        "Tôi không thể bảo vệ trái tim bạn khỏi đau thương và rỉ máu, nhưng tôi sẽ cùng bạn làm những điều thật ý nghĩa và tươi đẹp để làm lành vết thương ấy.",
        "Hãy mạnh mẽ lên cô gái - Be Stronger rồi mọi việc sẽ ổn thôi",
        "Hãy mạnh mẽ lên cậu - Be Stronger rồi mọi việc sẽ ổn thôi",
        "Ngày mai sẽ ổn thôi",
        "Nếu cậu cần người trò chuyện thì tớ luôn ở đây",
    ]
    for i in list_SOS:
        if i in question.lower():
            SOS = True
            data = random.choice(data_reply_SOS)
    
    if(SOS==True):
        return data
    else:
        for i in list_danger:
            if i in question.lower():
                danger = True
                data = random.choice(data_reply_darnger)+random.choice(Kaomoji)

        if(danger==True):
            return data
        else:
            for i in list_warn:
                if i in question.lower():
                    warn = True
                    data = random.choice(data_reply_warn)

            if(warn==True):
                return data
            else:
                choice_emoji = random.choice(check_list)
                for i in list:
                    if i in data.lower().split(" "):
                        ChatBot(question)

                for i in data.lower().split(" "):
                    if(i=="simsimi"):
                        data=data.replace("simsimi","relax")
                    if(i=="simsim"):
                        data=data.replace("simsim","ri")
                    if(i=="sim"):
                        data=data.replace("sim","ri")
                    if(i=="tôi"):
                        data=data.replace("tôi","tui")
                    if(i=="mày"):
                        data=data.replace("mày","you")


                if(choice_emoji=="True"):
                    data = data + " " + random.choice(Kaomoji)
                else:
                    data = data + " " + random.choice(emoji)
                return data
    
while(True):
    question = input("You: ")
    print(">> Bot: ",ChatBot(question))
    