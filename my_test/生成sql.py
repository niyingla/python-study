"""
public static void main(String[] args) {
//        //1时4分25秒 转成s
//        long time = 1*60*60 + 4*60 + 25;
//        System.out.println(time);
//        SpringApplication.run(ScheduleApplication.class,args);
        /**
         * 7392155100988377894
         * 2024.07.16 16:57:35
         * 2024.07.16 18:02:04
         * 1时4分25秒
         * update le_ai_live set end_time = '2024.07.16 18:02:04',duration = where room_id = '7392155100988377894';
         *
         */
        long time = timeToSecond("1时4分25秒");
        String sql = "update le_ai_live set end_time = '2024.07.16 18:02:04',duration = " + time + "where room_id = '7392155100988377894';";
        System.out.println(sql);
        String sql1 = "update le_live_review set end_time = '2024.07.16 18:02:04',duration = " + time + "where room_id = 'rpa_room_id';";
        System.out.println(sql1);
    }

    /**
     *
     * @param time 1时4分25秒 或者4分25秒 或者25秒 转成秒
     * @return
     */
    public static long timeToSecond(String time) {
        String[] split = time.split("时");
        long hour = 0;
        long minute = 0;
        long second = 0;
        if (split.length == 2) {
            hour = Long.parseLong(split[0]);
            split = split[1].split("分");
            minute = Long.parseLong(split[0]);
            split = split[1].split("秒");
            second = Long.parseLong(split[0]);
        } else {
            split = split[0].split("分");
            if (split.length == 2) {
                minute = Long.parseLong(split[0]);
                split = split[1].split("秒");
                second = Long.parseLong(split[0]);
            } else {
                split = split[0].split("秒");
                second = Long.parseLong(split[0]);
            }
        }
        return hour * 60 * 60 + minute * 60 + second;
    }
"""

#参数 2024.07.16 18:02:04 转成时间戳秒
def timeToSecond(param):
    split = param.split(" ")
    split1 = split[0].split("-")
    split2 = split[1].split(":")
    year = int(split1[0])
    month = int(split1[1])
    day = int(split1[2])
    hour = int(split2[0])
    minute = int(split2[1])
    second = int(split2[2])
    return year * 365 * 24 * 60 * 60 + month * 30 * 24 * 60 * 60 + day * 24 * 60 * 60 + hour * 60 * 60 + minute * 60 + second



if __name__ == '__main__':
    roomId = input("请输入roomId:")
    start_time = input("请输入开始时间:")
    end_time = input("请输入结束时间:")
    #计算时间差
    time = timeToSecond(end_time) - timeToSecond(start_time)

    sql = ("UPDATE le_ai_live SET end_time = '" + start_time + "',live_status = 1, duration = " + str(time)
           + " where room_id = '" + roomId + "';")
    print(sql)
    sql1 = ("UPDATE le_live_review SET end_time = '" + start_time + "',status = 1, duration = " + str(time)
           + " where rpa_room_id = '" + roomId + "';")
    print(sql1)
    # 等待客户端输入任意键退出
    input("Press any key to exit")
