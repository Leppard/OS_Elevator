package elevator;
import javax.swing.*;
import javax.swing.plaf.basic.BasicArrowButton;

import elevator.elevatorstart.clicklisten;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class elevatorsurface extends JPanel implements Runnable{
	JButton[] floor;
	JButton[] floorbutton;
	boolean[] isdooropen;
	boolean[] pressedfloor;
	int needup,needdown;
	int nowfloor;
	int goalfloor;
	int state;
	public static BasicArrowButton[] buttonup = new BasicArrowButton[19];
	public static BasicArrowButton[] buttondown = new BasicArrowButton[19];
	public  boolean[] upbutton = new boolean[20];
	public  boolean[] downbutton = new boolean[20];
	static int elenum = 0;
	public void run(){
		while (true){
			try 
			{
				Thread.sleep(500);
				if (upbutton[nowfloor] && state == 1)
				{
					Thread.sleep(500);
					opendoor();
					if (nowfloor != 19)
						buttonup[nowfloor].setBackground(Color.WHITE);
					floorbutton[nowfloor].setBackground(Color.WHITE);
					if (nowfloor != 0)
						buttondown[nowfloor-1].setBackground(Color.WHITE);
					upbutton[nowfloor] = false;
					needup--;
				}
				else
					if (downbutton[nowfloor] && state == 2)
					{
						Thread.sleep(500);
						opendoor();
						if (nowfloor != 0)
							buttondown[nowfloor-1].setBackground(Color.WHITE);
						if (nowfloor != 19)
							buttonup[nowfloor].setBackground(Color.WHITE);
						floorbutton[nowfloor].setBackground(Color.WHITE);
						downbutton[nowfloor] = false;
						needdown--;
					}
				if (needdown+needup == 0)
				{
					state = 0;
				}
				else
					if (state == 0)
					{
						if (needup != 0)
							state = 1;
						else
							state = 2;
					}
				if (state == 1)
				{
					elevatorgoup();
				}
				else
					if (state == 2)
					{
						elevatorgodown();
					}
			} catch (InterruptedException e){
				e.printStackTrace();
			}
		}
	}
	public void opendoor()
	{
		floor[nowfloor].setBackground(Color.GREEN);
		floor[nowfloor].setText("open");
		try {
			Thread.sleep(2000);
		} catch (InterruptedException e){
			e.printStackTrace();
		}
		floor[nowfloor].setBackground(Color.YELLOW);
		floor[nowfloor].setText("");
	}
	public void elevatorgoup()
	{
		if (nowfloor != 19)
		{
			floor[nowfloor].setBackground(Color.WHITE);
			nowfloor++;
			floor[nowfloor].setBackground(Color.yellow);
		}
		else
		{
			for (int i = 0; i < 20; i++)
				if (upbutton[i])
				{
					downbutton[i] = true;
					needup--;
					needdown++;
				}
			state = 0;
			if (needdown!= 0) state = 2;
		}
	}
	public void elevatorgodown()
	{
		if (nowfloor != 0)
		{
			floor[nowfloor].setBackground(Color.WHITE);
			nowfloor--;
			floor[nowfloor].setBackground(Color.yellow);
		}
		else
		{
			for (int i = 0; i < 20; i++)
				if (downbutton[i])
				{
					upbutton[i] = true;
					needdown--;
					needup++;
				}
			state = 0;
			if (needup!= 0) state = 1;
		}
	}
	public elevatorsurface(){
		setLayout(new GridLayout(21,2));
		pressedfloor = new boolean[20];
		nowfloor = 0;
		goalfloor = 0;
		state = 0;
		needup =0;
		needdown = 0;
		JLabel showtext = new JLabel("elevator",SwingConstants.CENTER);
		add(showtext);
		JLabel showfloor = new JLabel(elenum + 1 +"",SwingConstants.CENTER);
		add(showfloor);
		floor = new JButton[20];
		floorbutton = new JButton[20];
		for (int i = 19 ; i >= 0 ; i--)
		{
			floor[i] = new JButton(i+1+"");
			add(floor[i]);
			floor[i].setBackground(Color.white);
			floorbutton[i] = new JButton(i+1+"");
			floorbutton[i].addActionListener(new clicklisten(elenum,i));
			add(floorbutton[i]);
		}

		floor[nowfloor].setBackground(Color.yellow);
	}	
}
