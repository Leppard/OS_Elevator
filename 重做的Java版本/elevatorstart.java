package elevator;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.math.*;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.plaf.basic.BasicArrowButton;
public class elevatorstart extends JFrame {
	public static elevatorsurface[] elevator = new elevatorsurface[5];
	public elevatorstart() {
		setLayout(new GridLayout(1,6));
		Thread[] t = new Thread[5];
		for (int i = 0; i < 5 ; i++)
		{
			elevator[i] = new elevatorsurface();
			elevator[i].elenum ++;
			t[i] = new Thread(elevator[i]);
			t[i].start();
			add(elevator[i]);
		}
		JPanel panel = new JPanel();
		this.add(panel);
		panel.setLayout(new GridLayout(21,2));
		JLabel showinfo1 = new JLabel("1252964",SwingConstants.CENTER);
		panel.add(showinfo1);
		JLabel showinfo2 = new JLabel("ÀîÕêÁ¼",SwingConstants.CENTER);
		panel.add(showinfo2);
		JLabel labeltop = new JLabel("up",SwingConstants.CENTER);
		JLabel labelbottom = new JLabel("down",SwingConstants.CENTER);
		panel.add(labeltop);
		for (int i = 18; i >= 0 ; i --)
		{
			elevator[1].buttondown[i] = new BasicArrowButton(BasicArrowButton.SOUTH);
			elevator[1].buttondown[i].setBackground(Color.WHITE);
			elevator[1].buttondown[i].addActionListener(new clicklisten(6,i));
			panel.add(elevator[1].buttondown[i]);
			elevator[1].buttonup[i] = new BasicArrowButton(BasicArrowButton.NORTH);
			elevator[1].buttonup[i].setBackground(Color.WHITE);
			elevator[1].buttonup[i].addActionListener(new clicklisten(5,i));
			panel.add(elevator[1].buttonup[i]);
		}
		panel.add(labelbottom);
		this.setLocation(230, 100);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setSize(1000,590);
		this.setVisible(true);
	}
	public static void main(String[] args){
		JFrame frame = new elevatorstart();
	}
	public static class clicklisten implements ActionListener{
		private int elenum, floor;
		public clicklisten(int i, int j){
			elenum = i;
			floor = j;
		}
		public void actionPerformed(ActionEvent e)
		{
			if(elenum < 5)
			{
				elevator[elenum].floorbutton[floor].setBackground(Color.RED);
				if (floor > elevator[elenum].nowfloor && elevator[elenum].upbutton[floor] == false)
				{
					elevator[elenum].upbutton[floor] = true;
					elevator[elenum].needup++;
				}
				else
					if (floor <= elevator[elenum].nowfloor && elevator[elenum].downbutton[floor] == false)
					{
						elevator[elenum].downbutton[floor] = true;
						elevator[elenum].needdown++;
					}
			}
			else if (elenum == 5)
			{
				double max = 100;
				int choose = 0;
				for (int i = 0; i < 5; i++)
				{
					if (max > Math.abs(elevator[i].nowfloor - floor) && elevator[i].state != 2)
					{
						choose = i;
						max = elevator[i].nowfloor - floor;
					}
				}
				System.out.println("choose	:"+choose);
				elevator[choose].buttonup[floor].setBackground(Color.RED);
				if (floor <= elevator[choose].nowfloor && elevator[choose].state != 2 && elevator[choose].downbutton[floor] == false)
				{
					elevator[choose].downbutton[floor] = true;
					elevator[choose].needdown++;
				}
				else
					if (elevator[choose].upbutton[floor] == false)
					{
						elevator[choose].upbutton[floor] = true;
						elevator[choose].needup++;
					}
			}
			else
			{	double max = 100;
				int choose = 0;
				for (int i = 0; i < 5; i++)
				{
					if (max > Math.abs(elevator[i].nowfloor - floor) && elevator[i].state != 1)
					{
						choose = i;
						max = elevator[i].nowfloor - floor;
					}
				}
				System.out.println("choose	:"+choose);
				elevator[choose].buttondown[floor].setBackground(Color.RED);
				if (floor > elevator[choose].nowfloor && elevator[choose].state != 1 && elevator[choose].upbutton[floor + 1] == false)
				{
					elevator[choose].upbutton[floor + 1] = true;
					elevator[choose].needup++;
				}
				else
					if (elevator[choose].downbutton[floor + 1] == false)
					{
						elevator[choose].downbutton[floor + 1] = true;
						elevator[choose].needdown++;
					}
			}
		}
	}

}
