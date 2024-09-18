# Class Participation Exercise 2020-04-08 Refactoring

**Date:** 2024-09-17  
**Tags:** resources, reading, references, practice  
**Authors:** Neil Borle, Mitchell Home, Bronte Lee, Aaron Padlesky, Eddie Santos  
**Status:** published  
**Summary:** Individual, Assignments, Participation

----

### License
	•	Copyright 2012 Neil Borle, Mitchell Home, Bronte Lee, Aaron Padlesky, Eddie Santos

	•	Licensed under the Apache License, Version 2.0 (the “License”);
	•	you may not use this file except in compliance with the License.
	•	You may obtain a copy of the License at

	•	http://www.apache.org/licenses/LICENSE-2.0

	•	Unless required by applicable law or agreed to in writing, software
	•	distributed under the License is distributed on an “AS IS” BASIS,
	•	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	•	See the License for the specific language governing permissions and
	•	limitations under the License.


![Participation Exercise Image](../../content/images/old_participation/exer20200408refactoring.png)

```.java
public class ResponseObtainerObtainer {
 
    public static ResponseObtainer getResponseObtainer(
            MediaType media, LayoutInflater inflater,
            ViewGroup root) throws Exception {
 
        ResponseObtainer obtainer = null;
        int layout_id = -1;
        ViewGroup view = null;
        Class<? extends ResponseObtainer> obtainerClass = null;
 
        switch (media) {
            case TEXT:
                layout_id = R.layout.fragment_fulfill_text;
                obtainerClass = TextResponseObtainer.class;
                break;
            case AUDIO:
                layout_id = R.layout.fragment_fulfill_audio;
                obtainerClass = AudioResponseObtainer.class;
                break;
            case PHOTO:
                layout_id = R.layout.fragment_fulfill_photo;
                obtainerClass = PhotoResponseObtainer.class;
                break;
            default:
                // err....
                // TODO: Give an error response obtainer?
        }
 
        view = (ViewGroup) inflater.inflate(layout_id, root);
        obtainer = obtainerClass.getConstructor(ViewGroup.class)
                    .newInstance(view);
        return obtainer;
    }
}
```

List 1 Code Smell
Evident in this code:

Propose or draw a refactoring for this code.

Why would a MediaType (TEXT, AUDIO, PHOTO) still be necessary after a refactoring?