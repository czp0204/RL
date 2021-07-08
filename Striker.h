/** A test striker option without common decision
 * robot 8是Striker
 * 相对于前锋的坐标系 x轴正方向是朝向对方球门的 
 * 使用Lookliftandright 来辅助转向
 * 禁止封装新函数
 * 调试的时候在控制台输出打印的参数output_text
 * 底层函数是不能修改的
 * 用alientoball调整踢球的角度和位姿
 * 机器人的自定位可能有很大差别 进球后恢复到ready的状态 
 * 踢球的距离是固定的 需要自己测 在决赛时可以修改距离
 */


option(Striker)
{
  	// static Vector2f Goal=Vector2f(0,0);
	  // static Vector2f Goal1=Vector2f(1500,0);
  initial_state(start)
  {
    transition
    {
      if(state_time > 1000) //原来是1000 单位 ms 
        goto turnToBall;
    }
    action
    {
      HeadControlMode(HeadControl::lookForward);
      Stand();
      // OUTPUT_TEXT("开始啦，Look Forward!");
    }
  }

  state(turnToBall)
  {
    transition
    {// 如果看不到球的话
      if(theLibCodeRelease.timeSinceBallWasSeen > theBehaviorParameters.ballNotSeenTimeOut)
        goto searchForBall;
        OUTPUT_TEXT("看不到球,Search ball！");
      if(Transformation::fieldToRobot(theRobotPose,theBallModel.estimate.position).angle() < 5_deg)//球相对于机器人的位置.角度
        goto walkToBall;
        OUTPUT_TEXT("walkToBall! 球相对于机器人的位置.角度:");
        OUTPUT_TEXT(theBallModel.estimate.position.angle());
    }
    action
    {
      HeadControlMode(HeadControl::lookForward);
      WalkToTarget(Pose2f(80.f, 80.f, 80.f), Pose2f(Transformation::fieldToRobot(theRobotPose,theBallModel.estimate.position).angle(), 0.f, 0.f));
      OUTPUT_TEXT("it`s time toWalk To Target");
      // WalkToTarget(Pose2f(50.f, 50.f, 50.f), Pose2f(theBallModel.estimate.position.angle(), 0.f, 0.f));
      //两个参数是速度和目标位置，位置是相对机器人的位置
    }// 分别是角速度 x轴的速度 y轴的速度 trans 相对坐标和绝对坐标的相互转换转向球时不需要考虑球的位置，
    //只用调整到对准球的方向即可，所以theBallModel.estimate.position的
    
  }

  state(walkToBall) // 每次踢完球 球不一定正对着机器人 自己调整位置
  {
    transition
    {
      if(theLibCodeRelease.timeSinceBallWasSeen > theBehaviorParameters.ballNotSeenTimeOut)
        goto searchForBall;
         OUTPUT_TEXT("找球");
      if(theBallModel.estimate.position.norm() < 500.f)
       OUTPUT_TEXT("对齐球");
        goto alignToGoal;
    }
    action
    {
      HeadControlMode(HeadControl::lookForward);
      // WalkToTarget(Pose2f(80.f, 80.f, 80.f), Pose2f(Transformation::fieldToRobot(theRobotPose,theBallModel.estimate.position).angle(), 
      // 0.f, 0.f));// 走向球的函数
      WalkToTarget(Pose2f(50.f, 50.f, 50.f), Pose2f(theBallModel.estimate.position.angle(), 0.f, 0.f));
      // WalkToTarget(Pose2f(50.f, 50.f, 50.f), Pose2f(500, 0));// 走向球的函数
      //  WalkToTarget(Pose2f(50.f, 50.f, 50.f), 
      //  Pose2f(Transformation::fieldToRobot(theRobotPose,Goal1).angle(), 
      //  Transformation::fieldToRobot(theRobotPose,Goal1)));
       OUTPUT_TEXT("走向球");
    }
  }

  state(alignToGoal)// 将自己朝向对方的球门
  {
    transition
    {
      if(theLibCodeRelease.timeSinceBallWasSeen > theBehaviorParameters.ballNotSeenTimeOut)
        goto searchForBall;
      if(std::abs(theLibCodeRelease.angleToGoal) < 10_deg && std::abs(theBallModel.estimate.position.y()) < 100.f)
        goto alignBehindBall;
    }
    action
    {
      HeadControlMode(HeadControl::lookForward);
      WalkToTarget(Pose2f(100.f, 100.f, 100.f), Pose2f(theLibCodeRelease.angleToGoal, theBallModel.estimate.position.x() - 300.f, theBallModel.estimate.position.y()));
      OUTPUT_TEXT("align to 球门");
    }//Thegoal is球门
  }

  state(alignBehindBall)// 走到球后边 不好的地方是 每次丢掉球 都要重新找球 不如ready的写法
  {
    transition
    {
      if(theLibCodeRelease.timeSinceBallWasSeen > theBehaviorParameters.ballNotSeenTimeOut)
        goto searchForBall;
      if(theLibCodeRelease.between(theBallModel.estimate.position.y(), 20.f, 50.f)
         && theLibCodeRelease.between(theBallModel.estimate.position.x(), 140.f, 170.f)
         && std::abs(theLibCodeRelease.angleToGoal) < 2_deg)
        goto kick;
    }
    action
    {
      theHeadControlMode = HeadControl::lookForward;
      WalkToTarget(Pose2f(80.f, 80.f, 80.f), Pose2f(theLibCodeRelease.angleToGoal, theBallModel.estimate.position.x() - 150.f, theBallModel.estimate.position.y() - 30.f));
    }
  }

  state(kick)// 判断kick的条件是有一定的差距的 
  {
    transition
    {
      if(state_time > 3000 || (state_time > 10 && action_done))
        goto start;
    }
    action
    {
      HeadControlMode(HeadControl::lookForward);
      InWalkKick(WalkKickVariant(WalkKicks::forward, Legs::left), Pose2f(theLibCodeRelease.angleToGoal, theBallModel.estimate.position.x() - 160.f, theBallModel.estimate.position.y() - 55.f));
    }//原来是球 -55.f
  }

  state(searchForBall)
  {
    transition
    {
      if(theLibCodeRelease.timeSinceBallWasSeen < 300)
        goto turnToBall;
    }
    action
    {
      HeadControlMode(HeadControl::lookForward);
      //to do 原地转向找球
      WalkAtRelativeSpeed(Pose2f(1.f, 0.f, 0.f));
      OUTPUT_TEXT("searchingball");
    }
  }
}
