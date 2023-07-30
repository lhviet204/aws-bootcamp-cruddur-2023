-- this file was manually created
INSERT INTO public.users (display_name, handle, cognito_user_id, email)
VALUES
  ('Andrew Brown', 'andrewbrown' ,'MOCK', 'andrew@emailpro.co'),
  ('Tony Stark', 'tony' ,'MOCK', 'tony@emailpro.co'),
  ('Andrew Bayko', 'bayko' ,'MOCK', 'bayko@emailpro.co'),
  ('Londo Mollari', 'londo','MOCK', 'lmollari@centari.com'),
  ('Altern Andrew ', 'altandrew' ,'MOCK', 'altandrew@emailpro.co'),
  ('Lu Blue', 'lublue','1401e067-d4ab-409e-b7f3-6f9bc2fc7f7a', 'mrlu204@gmail.com');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'andrewbrown' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  ),
  (
    (SELECT uuid from public.users WHERE users.handle = 'altandrew' LIMIT 1),
    'I am the other Andrew!',
    current_timestamp + interval '10 day'
  );