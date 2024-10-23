# QuickiDaily
- Originally named "Organizer" hence the file names
- Use for Congressional App Competition

**Purpose**
- Quickly creates an efficient and effective daily schedule
- More flexible and personal through short commands

**Commands**
- (note that brackets are to indicate a user input)
  1) none
     - Create an event at a specified time
     - Input format: [first letter of am/pm][time] [title of event]
     - example:
       p110 event1
        --> Creates event called "event1" at 1:10PM
  2) d
     - First method of 'd': Delete event at a specified time
     - Input format: d [first letter of am/pm][time]
     - Example:
       d a1200
       --> Deletes event listed at 12:00AM
  3) d
     - Second method of 'd': Delete multiple events in a given range
     - Input format: d [time 1] [time 2]
     - Both time 1 and time 2 are inclusive in the range
     - Example:
       d a1100 p600
       --> Deletes all events at and between 11:00AM and 6:00PM
  5) e
     - First method of 'e': to change an event's time
     - Input format: e [time 1] [time 2]
     - Example:
       e p125 p250
       --> Changes the event time at 1:25PM to 2:50PM
  6) e
     - Second method of 'e': to shift a range of events' times by an amount of time.
     - Input format: e [low boundary of time] [high boundary of time] [time shift in minutes]
     - Both bounds inclusive 
     - Example:
       e a1100 p300 45
       --> Increments all events' times between 11:00AM to 3:00PM (Including 11:00AM and 3:00PM) by 45 minutes
       Result: 11:45AM, time2+45, time3+45, ..., 3:45PM

  7) n
     - Creates a list of notes under an event
     - Input format: n [first letter of am/pm][time]
     - Example:
       n p701
       --> Creates list at 7:01PM where you can add notes
       To add a note:
       - Input format: - [information]
       - Example:
         - Shopping list
         --> Adds the note "Shopping list"
      - Notes are numbered, indicated its index

      To edit a note:
      - Input format: [index] [replacement information]
      - Example:
        1 New shopping list
        --> Renames the first note to "New shopping list"

     To delete a note:
     - Input format: d [index]
     - Example:
       d 2
       --> Deletes the second note

     To save the list of notes:
     - Input format: n
     - Example:
       n
       --> Basically press again to save and exit a list

8) r
   - Reset the schedule to its initally saved information
   - Input format: r
   - Example:
    r
     --> If you made any edits, those edits are lost and you can "restart" again

9) s
   - Saves the schedule (onto the file "Organizer_save") and displays the formatted schedule on the file "Organizer_display"
   - Input format: s
   - Example:
     s
     --> When you are done with the schedule, input s 

       
     
       
  

