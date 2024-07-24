"""
 String tenantKey = "wpLHbUCwAAjnMUfpdw_xR2F1-PW8Lutw";
 Long timestamp = System.currentTimeMillis();
 System.out.println("timestamp:"+ timestamp);
 TreeMap<String, String> sortMap = new TreeMap<>(String::compareTo);
 sortMap.put(TENANT_KEY, tenantKey);
 sortMap.put(TIMESTAMP, timestamp.toString());
 List<String> paramList = new ArrayList<>();
 sortMap.forEach((key, value) -> {
     StringBuilder sb = new StringBuilder();
     sb.append(key).append("=");
     if (value != null) {
         sb.append(value);
     }
     paramList.add(sb.toString());
 });
 paramList.add("key=" + "zdfhzsjfgzxfzhbfk4375sdfcxvkj");
 String paramText = Joiner.on("&").join(paramList);
 System.out.println("加密源串:"+ paramText);
 String paramSign = MD5.create().digestHex(paramText, StandardCharsets.UTF_8);
 System.out.println("加密源串:"+ paramSign);

"""
import hashlib
# 以上java代码生成python代码
import time
from hashlib import md5
from collections import OrderedDict
from urllib.parse import quote

TENANT_KEY = "tenantKey"
TIMESTAMP = "timestamp"


def generate_md5(paramText):
    # 创建 MD5 哈希对象
    md5_hash = hashlib.md5()
    # 更新哈希对象
    md5_hash.update(paramText.encode('utf-8'))
    # 获取十六进制表示的哈希值
    return md5_hash.hexdigest()

if __name__ == '__main__':
    sortMap = OrderedDict()
    sortMap[TENANT_KEY] = "wpLHbUCwAAjnMUfpdw_xR2F1-PW8Lutw"
    sortMap[TIMESTAMP] = str(int(time.time() * 1000))
    print("timestamp:", sortMap[TIMESTAMP])
    paramList = []
    for key, value in sortMap.items():
        sb = key + "="
        if value:
            sb += value
        paramList.append(sb)
    paramList.append("key=zdfhzsjfgzxfzhbfk4375sdfcxvkj")
    paramText = "&".join(paramList)
    print("加密源串:", paramText)
    paramSign = generate_md5(paramText)
    print("加密后验签:", paramSign)
    #等待客户端输入任意键退出
    input("Press any key to exit")

